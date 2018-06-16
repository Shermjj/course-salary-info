import dash
import pandas as pd


app = dash.Dash()
app.title = 'Graduate Employment Data'
server = app.server
app.config.supress_callback_exceptions = True

app.scripts.config.serve_locally = True

app.css.append_css({'external_url': 'https://codepen.io/shermjj/pen/ZREaLY.css'})
app.css.append_css({'external_url': 'https://fonts.googleapis.com/css?family=Open+Sans'})
app.css.append_css(
    {'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.1/components/message.min.css'})
app.css.append_css(
    {'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.1/components/header.min.css'})
app.css.append_css(
    {'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.1/components/icon.min.css'})

df = pd.read_pickle('./final_v1.02.pkl')
