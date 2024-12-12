from google.colab import files
import pandas as pd
import io
from openai import OpenAI
f = files.upload()

df = pd.read_csv(io.BytesIO(f['goodreads (1).csv']))
df.head()

# Replace with your actual AIPROXY_TOKEN
AIPROXY_TOKEN = "YOUR_AIPROXY_TOKEN"

client = OpenAI(api_key=AIPROXY_TOKEN, base_url="https://aiproxy.sanand.workers.dev/openai/")

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "Write a Python script that uses an LLM to analyze, visualize, and narrate a story from a dataset.\ndata may be any  csv formatted data. and result should be store another file .analyze, visualize and narrate a story  should done sequenseally."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "indexbook_idgoodreads_book_idbest_book_idwork_idbooks_countisbnisbn13authorsoriginal_publication_yearoriginal_titletitlelanguage_codeaverage_ratingratings_countwork_ratings_countwork_text_reviews_countratings_1ratings_2ratings_3ratings_4012767052276705227927752724390234839780439023480.0Suzanne Collins2008.0The Hunger GamesThe Hunger Games (The Hunger Games, #1)eng4.3447806534942365155254667151279365600921481305123346407994914395549349780439554930.0J.K. Rowling, Mary GrandPré1997.0Harry Potter and the Philosopher's StoneHarry Potter and the Sorcerer's Stone (Harry Potter, #1)eng4.44460247948000657586775504101676455024115631823418654186532122582263160158499780316015840.0Stephenie Meyer2005.0TwilightTwilight (Twilight, #1)en-US3.57386683939168249500945619143680279331987507334265726573275794487611200819780061120080.0Harper Lee1960.0To Kill a MockingbirdTo Kill a Mockingbirdeng4.253198671334089672586604271174154468351001952454671467124549413567432735679780743273560.0F. Scott Fitzgerald1925.0The Great GatsbyThe Great Gatsbyeng3.8926836642773745519928623619762160615893601     "
        }
      ]
    }
  ],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
