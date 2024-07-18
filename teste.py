import nltk

nltk.data.path.append("./vader_lexicon")

# Verificar o NLTK data path
print(nltk.data.path)

from nltk.sentiment.vader import SentimentIntensityAnalyzer



# Inicializar o analisador de sentimentos VADER
sid = SentimentIntensityAnalyzer()

# Exemplos de texto para análise
text = "Assessing proficiency in programming languages and related concepts reveals strong skills in Python, Java, and JavaScript. Demonstrated understanding of object-oriented programming, memory management, and efficient algorithms highlights a focused approach to building robust solutions."
text1 = "The student's understanding of unit testing, integration testing, and other essential testing practices, including test automation frameworks and test execution, appears to be limited, indicating a need for improvement in handling critical aspects of software quality assurance."

# Realizar a análise de sentimento
scores1 = sid.polarity_scores(text)
scores2 = sid.polarity_scores(text1)

# Exibir os resultados
print(f"Scores de Sentimento para text:\n{scores1}")
print(f"Scores de Sentimento para text1:\n{scores2}")
