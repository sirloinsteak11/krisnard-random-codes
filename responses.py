import api

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'sex!random':
        return api.random_doujin()

    if p_message == 'sex!help':
        return "use sex!random to generate a random code from krisnards favorites"