import google.generativeai as genai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration sécurisée
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ ERREUR: Clé API Gemini non trouvée dans le fichier .env")
    exit(1)

genai.configure(api_key=api_key)

def analyser_par_gemini(test_name, error_message):
    prompt = f"""
    Le test nommé '{test_name}' a échoué avec le message suivant :
    {error_message}

    Donne-moi une analyse probable de la cause de l'échec et des suggestions pour le corriger.
    """

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Erreur lors de l'analyse : {e}"

# Test
print("🔍 Analyse en cours...")
result = analyser_par_gemini("Failing Test", "This test is intentionally failed")
print("\n📋 Résultat:")
print(result)