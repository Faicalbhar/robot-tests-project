import json

def create_jira_ticket_simulated(test_name, message, gpt_analysis):
    ticket = {
        "project": "TEST",
        "summary": f"[Bug] Test échoué : {test_name}",
        "description": f"""
        Le test **{test_name}** a échoué.

        ❌ Message d'erreur :  
        {message}

        🧠 Analyse IA :  
        {gpt_analysis}
        """,
        "priority": "High"
    }

    with open(f"jira_ticket_{test_name.replace(' ', '_')}.json", "w") as f:
        json.dump(ticket, f, indent=4)

    print(f"Ticket simulé généré pour {test_name}")

# Exemple d'appel
create_jira_ticket_simulated("Failing Test", "This test is intentionally failed", "Ceci est un test d'échec simulé.")
