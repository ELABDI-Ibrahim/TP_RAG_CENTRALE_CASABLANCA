# Q2: recherche documentaire + scores
# Ok so here we need to search through our vector database and get relevant documents
# The tricky part is we also need the scores to see how good the matches are

from langchain_community.vectorstores import Chroma
from embedder import Embedder
from typing import List, Tuple, Dict, Any


class DocumentRetriever:
    """
    This class helps us find the most relevant documents from our vector database.
    Think of it like a smart search engine that understands the meaning of your question!
    """
    
    def __init__(self, vectorstore_dir: str, embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize the retriever. We need to know where the database is and which model to use.
        
        Args:
            vectorstore_dir: where we saved all our document embeddings (the vector database)
            embedding_model_name: the model we used when we indexed the documents (must be the same!)
        """
        self.vectorstore_dir = vectorstore_dir
        self.embedder = Embedder(model_name=embedding_model_name)
        
        # Load the existing vector database
        # This is important: we're not creating a new one, we're loading what we already built
        self.vectorstore = Chroma(
            persist_directory=self.vectorstore_dir,
            embedding_function=self.embedder.embedding_model
        )
        
        print(f"✅ Retriever ready! Loaded database from: {vectorstore_dir}")
    
    
    def search_documents(self, query: str, k: int = 5) -> List[Any]:
        """
        Basic search - just give me the top k most similar documents.
        Simple and straightforward, no fancy stuff here.
        
        Args:
            query: what the user wants to know (their question)
            k: how many results to return (default is 5, seems reasonable)
        
        Returns:
            List of the most relevant documents
        """
        # Just do a simple similarity search
        results = self.vectorstore.similarity_search(query, k=k)
        return results
    
    
    def search_with_scores(self, query: str, k: int = 5) -> List[Tuple[Any, float]]:
        """
        This is the main method for Q2!
        Returns documents WITH their similarity scores so we know how confident we are.
        
        The scores tell us: "Hey, this document is X% similar to your question"
        Lower scores = better match (it's a distance measure, so closer = better)
        
        Args:
            query: the user's question
            k: number of results we want back
        
        Returns:
            List of tuples: (document, score)
            Example: [(doc1, 0.23), (doc2, 0.45), ...] where lower scores are better
        """
        # This method returns both the documents AND the similarity scores
        # Perfect for what we need in Q2!
        results_with_scores = self.vectorstore.similarity_search_with_score(query, k=k)
        
        return results_with_scores
    
    
    def search_with_relevance_scores(self, query: str, k: int = 5) -> List[Tuple[Any, float]]:
        """
        Alternative method that returns relevance scores (higher = better).
        Some people prefer this because higher numbers = better match feels more intuitive.
        
        Args:
            query: user's question
            k: how many documents to retrieve
            
        Returns:
            List of (document, relevance_score) where higher is better
        """
        # This one is cool because the scores are between 0 and 1
        # 1 = perfect match, 0 = totally unrelated
        results = self.vectorstore.similarity_search_with_relevance_scores(query, k=k)
        return results
    
    
    def detailed_search(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """
        Returns everything in a nice organized dictionary format.
        Makes it easier to work with the results and see what we got.
        
        Args:
            query: the search question
            k: number of results
            
        Returns:
            List of dictionaries with all the info organized nicely
        """
        # Get the raw results with scores
        results_with_scores = self.search_with_scores(query, k=k)
        
        # Now let's organize this into something more readable
        detailed_results = []
        
        for i, (doc, score) in enumerate(results_with_scores, 1):
            # For each result, let's extract the useful info
            result_dict = {
                'rank': i,  # what position is this result? 1st, 2nd, 3rd...
                'content': doc.page_content,  # the actual text content
                'score': round(score, 4),  # the similarity score (rounded so it's not crazy long)
                'metadata': doc.metadata,  # any extra info about where this came from
                'source': doc.metadata.get('source', 'Unknown'),  # which PDF file?
                'page': doc.metadata.get('page', 'N/A')  # which page in the PDF?
            }
            detailed_results.append(result_dict)
        
        return detailed_results
    
    
    def search_and_print_results(self, query: str, k: int = 5):
        """
        Helper method for testing - search and automatically print the results nicely.
        Makes it easy to see what we're getting back during development.
        
        Args:
            query: the question to search for
            k: how many results to show
        """
        print(f"\n{'='*80}")
        print(f"🔍 Searching for: '{query}'")
        print(f"📊 Retrieving top {k} results...")
        print(f"{'='*80}\n")
        
        # Get the detailed results
        results = self.detailed_search(query, k=k)
        
        # If we didn't find anything, let the user know
        if not results:
            print("❌ No results found. Maybe the database is empty?")
            return
        
        # Print each result in a nice readable format
        for result in results:
            print(f"Result #{result['rank']}")
            print(f"  📄 Source: {result['source']}")
            print(f"  📖 Page: {result['page']}")
            print(f"  🎯 Score: {result['score']} (lower = better match)")
            print(f"  📝 Content preview: {result['content'][:200]}...")  # just show first 200 chars
            print(f"  {'-'*76}")
        
        print(f"\n✅ Found {len(results)} relevant document(s)!\n")
    
    
    def get_context_for_llm(self, query: str, k: int = 3) -> str:
        """
        Special method to prepare context for the LLM (we'll need this for Q3).
        Takes the top k documents and combines them into one text block.
        
        Why? The LLM needs context to answer questions, so we give it the relevant chunks!
        
        Args:
            query: user's question
            k: how many documents to use as context (3-5 is usually good)
            
        Returns:
            A single string with all the relevant context combined
        """
        # Get the best matching documents
        results = self.search_documents(query, k=k)
        
        # Combine them into one big context string
        # We'll add some separators so the LLM knows they're different chunks
        context_parts = []
        for i, doc in enumerate(results, 1):
            # Add a clear marker between different document chunks
            context_parts.append(f"--- Document {i} ---\n{doc.page_content}\n")
        
        # Join everything together
        full_context = "\n".join(context_parts)
        
        return full_context
    
    
    def filter_by_score_threshold(self, query: str, threshold: float = 0.5, max_results: int = 10) -> List[Tuple[Any, float]]:
        """
        Only return documents that are "good enough" based on a score threshold.
        Sometimes we don't want mediocre matches, only the really good ones!
        
        Args:
            query: the search query
            threshold: only return docs with score below this (remember, lower = better)
            max_results: don't return more than this many docs
            
        Returns:
            Filtered list of (document, score) tuples
        """
        # Get a bunch of results first
        all_results = self.search_with_scores(query, k=max_results)
        
        # Filter to only keep the good ones
        # Remember: lower score = better, so we keep scores BELOW the threshold
        filtered_results = [(doc, score) for doc, score in all_results if score <= threshold]
        
        return filtered_results


# Just a quick test function to make sure everything works
def test_retriever():
    """
    Quick test to make sure the retriever is working.
    You can call this to debug if something seems broken.
    """
    print("🧪 Running a quick test of the retriever...")
    
    # These paths should match your actual setup
    retriever = DocumentRetriever(vectorstore_dir="./vectorstore")
    
    # Try a test query
    test_query = "What is artificial intelligence?"
    retriever.search_and_print_results(test_query, k=3)
    
    print("✅ Test complete!")


# If you run this file directly, it will do a test
if __name__ == "__main__":
    test_retriever()
