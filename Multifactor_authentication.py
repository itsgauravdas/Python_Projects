import pyotp 
"""
A Python library for generating and verifying 
one-time passwords (OTPs) based on the TOTP 
(Time-based OTP) and HOTP (HMAC-based OTP) algorithms. 
It's commonly used in 
two-factor authentication (2FA) systems.
"""
import argparse
"""
A standard Python library used for parsing 
command-line arguments. It allows you to create 
user-friendly 
command-line interfaces for your scripts.
"""
import json

SECRET_STORAGE_FILE = "secret.json"

def generate_secret_key():
    return pyotp.random_base32()

def generate_totp(secret_ket, algorithm = 'SHA1', digits = 6, interval = 30):
    totp = pyotp.TOTP(secret_ket, digits=digits, interval=interval,
                      digest = algorithm)
    return totp.now()

def verify_totp(secret_key, code, algorithm = 'SHA1', digits = 6, interval = 30, window = 1):
    totp = pyotp.TOTP(secret_key, digits=digits, interval=interval,
                      digest = algorithm)
    return totp.verify(code, valid_window=window)

def save_secret(secret_key, filename):
    data = {'secret_key': secret_key}
    with open(filename, 'w') as file:
        json.dump(data,file)
    return f'Secret key saved to {filename}'

def load_secret(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data['secret_key']
    except FileNotFoundError:
        print(f'Secret key file "{filename}" not found.')
        return None

def main():
    parser = argparse.ArgumentParser(description='Multi-Factor Authentication (MFA) Generator')
    
    parser.add_argument('--generate_secret', action='store_true', help='Generate a new secret key')
    parser.add_argument('--generate', action='store_true',
                        help='Generate a TOTP code')
    parser.add_argument('--verify', action='store_true',help='Verify a TOTP code')
    parser.add_argument('--algorithm', choices=['SHA1', 'SHA256', 'SHA512'], default='SHA1', help='Hash algorithm for TOTP')
    parser.add_argument(
        '--digits', type=int, choices=[6, 8], default=6, help='Number of digits in TOTP code')
    parser.add_argument('--interval', type=int, default=30,
                        help='Time interval for TOTP code generation')
    parser.add_argument('--window', type=int, default=1,
                        help='Verification window for TOTP codes')
    parser.add_argument('--save', action='store_true',help='Save secret key to a file')
    parser.add_argument('--load', action='store_true',
                        help='Load secret key from a file')
    
    args = parser.parse_args()
    
    if args.generate_secret:
        secret_key = generate_secret_key()
        print(f"Generated secret key: {secret_key}")
        if args.save:
            save_result = save_secret(secret_key, SECRET_STORAGE_FILE)
            print(save_result)
        return

    secret_key = None
    # if args.load:
    #     secret_key = load_secret(SECRET_STORAGE_FILE)
    #     if secret_key is None:
    #         return
    # elif args.generate or args.verify:
    #     secret_key = input('Enter your secreat key').strip()
    #     if args.save:
    #         save_result = save_secret()
    #         print(save_result)
    # else:
    #     print('Please specify either --generate or --verify.')
    #     return
    
    if args.generate:
        secret_key = input('Please enter the key : -')
        code = generate_totp(secret_key, args.algorithm, args.digits, args.interval)
        print(f'Generated TOTP code: {code}')
        
    
            
    if args.verify:
        code_to_verify = input('Please enter the totp : -')
        secret_key = input('Please enter the key : -')
        result = verify_totp(secret_key, code_to_verify,
                             args.algorithm, args.digits, args.interval, args.window)
        
        if result:
            print('TOTP code is valid.')
        else:
            print('TOTP code is NOT valid.')
            
if __name__ == '__main__':
    main()
    
            


        
    



