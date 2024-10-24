import requests

def claim_tokens(message_body, formatted_phone_number):
    # Memeriksa apakah message_body dimulai dengan 'claimtokens_'
    if message_body.lower().startswith('claimtokens_'):
        parts = message_body.split('_')
        phone_number = formatted_phone_number
        order_sn = parts[1] if len(parts) > 1 else None

        # Validasi order_sn
        if not order_sn:
            print('Invalid order number. Please provide a valid order number.')
            return

        api_url = 'https://yuksyari.in/api/userzoom/zoom-personal-tokens/claimtokens'  # Ganti dengan URL API yang sesuai

        try:
            # Mengirimkan request POST ke API
            response = requests.post(api_url, json={
                'phoneNumber': phone_number,
                'ordersn': order_sn
            })

            # Memastikan response tidak mengandung error HTTP
            response.raise_for_status()

            # Mendapatkan data dari response JSON
            data = response.json()
            api_message = data.get('message', 'No message returned')
            tokens = data.get('tokens', None)
            tokens_amount = tokens.get('amount', 0) if tokens else 0

            # Mencetak hasil
            print(f'API Response: {api_message}\nTokens claimed: {tokens_amount}')

        except requests.exceptions.RequestException as e:
            print(f'Error claiming tokens: {e}')

            if e.response:
                error_data = e.response.json()
                errors = error_data.get('errors', None)
                error_message = ', '.join(errors) if errors else error_data.get('message', 'Unknown error')
                print(f'Error: {error_message}')
            else:
                print('Failed to claim tokens due to server error.')

# Contoh penggunaan fungsi
if __name__ == "__main__":
    message_body = 'claimtokens_240914VEGEM182'  # Ganti dengan data contoh
    formatted_phone_number = '6281515814752'  # Ganti dengan nomor telepon contoh
    claim_tokens(message_body, formatted_phone_number)
