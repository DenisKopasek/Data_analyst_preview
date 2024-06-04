import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Load the data
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, 'Data Analyst Take Home Exam Data.csv')
data = pd.read_csv(data_path)


# Function to extract top 5 articles based on number of occurrences in 'headline' and their keywords
def get_top_articles_keywords(section):
    section_data = data[data['section'] == section]
    top_articles = section_data['headline'].value_counts().nlargest(5).index.tolist()
    top_keywords = section_data[section_data['headline'].isin(top_articles)]['topicKeywords']
    
    # Collect all keywords from the top articles
    keywords = []
    for keywords_list in top_keywords:
        keywords.extend(keywords_list.split('|'))
        
    return keywords

# Generate word clouds for each section
sections = data['section'].unique()
for section in sections:
    keywords = get_top_articles_keywords(section)
    
    # Create word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(keywords))
    
    # Display word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Word Cloud for {section}')
    plt.axis('off')
    plt.show()
