import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "fuel-ua-3da49",
  "private_key_id": "909bb364fe8d750448fff245c5609746ab242d20",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDfg5yorWatWwMc\nt90TsRW/do7Q5Xl6FdiWt2XpkpEAUuiuVmMp/ldgMveawm6EmfFeeELRQGi9Ay6L\nBLdPU4+V1jnD77plKq4NMO1K7DIyLV0CQt2P+Gjfe1rohy6XZj4NkyzoqfoPWisv\nMriZ7WkdaO96UasI6JHbaanpGXA3ZgJB8c/LzgF5lN3PtTkfM3rg8h4o/nsWUJYi\n6tf8SIGEaqokmcUwOoP8B1/ZvF3TQaTiZfFYnFttdK9drdseqqPmh5rSiL/inxgj\nRs7gyZnWm0E96Qgatasn8PV50L2HrAivGpHZHYVOCwH11yv0JrxQvf7Jj4HaMx72\npAalkrblAgMBAAECggEAA1RHsZV/ntu+WfT9JILHPaZWQz31HMCVjM0nhfP1F/RO\n20XrIorTd1na/qGgbsuHi64uj0UD1QjmmRMqvdI9+cU1RWSyjzjfBdBG6zjwbcyS\nLZXxtz1ue8xaaCCXV5GiIVFMt8chs+KBG9SyvjbfPB0ThWwQ/Z16irJHYchLYm/U\nkb3f7OrBDaz2bNTvBu79eJaT3xwYGoHCG5qkAr9KP2fMWv2Y/rT/tpqOdjnQfaxz\nPHWlZ7m44ykJVupOR6SKl/d1xhOtce23nVVAKGnp+tUs8dfJMBZ2eTpCtsjD46jr\ndCnbOp7rEw5Dz34NcGwovxpnLI5nQ0120GA7EHnycwKBgQD76fIPXh2eN4cWfcNk\nOYFw1L/XLoryj6RePxPKxn6EKqQ5U2dZBScglkZZvINAvZWKtTIZB6OmgogR3sCh\nIyDaWSPjJ09LZFvgT6UbEUHfuCSmGJ4lYgPW+tMJjGJf80I43k2m/uF9hcQIsgNp\n4YMqmvMXBM8Fu/KCiufu/UX6BwKBgQDjI70NdBxa7Zri9DopjS51VMiDdx3aRygw\nXVPwp3uqYnYJSJ7d563UtNbRMllmpiTZNLUgS0GJ+68/qqQB6xA3TUyIXd+VujtL\nqDiK20TWYJjYKGEJp7I/9HP/rAFPszvukILygeeqbZStto3MhpJNwyDOmmwAED/3\n8cbRDsr8swKBgGqUBLwptmAs3/NNC/CIP9JLwEo6v8B1szXIfAgrSHWEUOyL88p+\n2pn32hW3ItSuIOmJVYOvbrZQvV7KHjdOVGTsl7lP9UVRVWmmaJT2DSeokaDQA4CP\nYk5+2fBNO4Watma27qV7ak0f3dtL7RPLvCG3YqdXenrTlHtUZ2H+N6/bAoGAe5da\nqxNeyms3N/7EFw/nE5jKch5CdB770zU1E2FOfOuOZobJSt1hTLgJm1LWKnCE5Fs1\noxjP1JDKTs4+53xMGotI9Xp+yi3HTed+vK+KyUtOX2+5PVOuPfZ5l8iz/fX8ylZ/\nqgzdTXLKz6rhhUREH2PpWgHUekRdSkCYefCeqtkCgYBqafl8OfCMLP7ibe0cEOtr\neGPyihOsLe0EcOLPFz21Z0ce6mw+IuSrPq71oQ/jPwtMlN/pdwu82Fpo7LN5X/D9\n3M4KbO2jDI6Y8ZhPJQPb8MWchiA5/q1vIOgZf+zNYcEy/QAXJMuUMMSYh2YVCzEV\nvCBQCDL/uWa63W08P+OoUw==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-6xpwf@fuel-ua-3da49.iam.gserviceaccount.com",
  "client_id": "109650331377390949839",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6xpwf%40fuel-ua-3da49.iam.gserviceaccount.com"
})
# Initialize the app with a service account, granting admin privileges

ref = firebase_admin.initialize_app(cred)



#ref = db.reference('/company')
print(ref)
