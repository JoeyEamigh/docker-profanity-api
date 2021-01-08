from fastapi import FastAPI
from profanity_check import predict, predict_prob
from better_profanity import profanity

app = FastAPI()

@app.get("/")
async def read_root(query: str):
  prediction = predict_prob([query])[0]
  leetSp33k = profanity.contains_profanity(query)
  if prediction > .5:
    return True
  else:
    if leetSp33k:
      return True
    else:
      return False