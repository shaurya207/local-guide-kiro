class Agent:
    def __init__(self, context_file):
        with open(context_file, 'r') as f:
            self.context = f.read()

    def run(self, query):
        # Simple keyword-based response
        query_lower = query.lower()
        if 'food' in query_lower:
            return "Popular street foods in Delhi include Golgappe at Chandni Chowk, Chole Bhature at Sita Ram Diwan Chand, Parathas at Paranthe Wali Gali, and Momos in Lajpat Nagar."
        elif 'slang' in query_lower:
            return "Local slang in Delhi: 'Bhai' is used casually, 'Scene kya hai?' means 'what is going on?', and 'Jugaad' means a smart workaround."
        elif 'culture' in query_lower:
            return "Delhi is the capital city of India and is famous for its street food and culture."
        else:
            return "I'm here to help with information about food, slang, or local culture in Delhi. Please ask something related!"