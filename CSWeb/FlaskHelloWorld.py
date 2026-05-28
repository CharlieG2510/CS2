from flask import Flask, render_template,request  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    #print(app.url_map)
    #print('line 17')            # Print statements go to your console
    
    #return render_template("index.html")
    return "Hello, World!"  # Return this string as a response to the client
    


@app.route('/survey')   # URL '/' to be handled by main() route handler
def survey():
    return render_template("fms.html")

@app.route('/collect_favorites')   # URL '/' to be handled by main() route handler
def collect_favorites():
    fav_type = request.args.get('fav_type')
    num_of_movies = request.args.get('num_of_movies')
    fav_movie = request.args.get('fav_movie')

    print(f'fav type:{fav_type}')
    print(f'num of movies:{num_of_movies}')
    print(f'fav movie:{fav_movie}')

    column = f'''{fav_type}, {num_of_movies}, {fav_movie}
'''
    with open('saved_favorites.csv', 'a') as sav_favs:
        sav_favs.write(column)
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Thank You</title>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Lato:wght@300;400&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    :root {{
      --cream: #faf7f2;
      --ink: #1a1714;
      --gold: #c9a84c;
      --muted: #8a8279;
    }}

    body {{
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: var(--cream);
      font-family: 'Lato', sans-serif;
      overflow: hidden;
    }}

    body::before {{
      content: '';
      position: fixed;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
      background-size: 180px;
      pointer-events: none;
      z-index: 0;
    }}

    .card {{
      position: relative;
      z-index: 1;
      text-align: center;
      padding: 5rem 4rem;
      max-width: 480px;
      width: 90%;
      animation: rise 0.9s cubic-bezier(0.16, 1, 0.3, 1) both;
    }}

    .card::before, .card::after {{
      content: '';
      position: absolute;
      width: 40px;
      height: 40px;
      border-color: var(--gold);
      border-style: solid;
      opacity: 0.6;
      animation: corners 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.3s both;
    }}
    .card::before {{ top: 0; left: 0; border-width: 1px 0 0 1px; }}
    .card::after  {{ bottom: 0; right: 0; border-width: 0 1px 1px 0; }}

    .ornament {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1rem;
      margin-bottom: 2.5rem;
      opacity: 0;
      animation: fade 0.6s ease 0.5s forwards;
    }}
    .ornament-line {{
      height: 1px;
      width: 48px;
      background: linear-gradient(90deg, transparent, var(--gold));
    }}
    .ornament-line:last-child {{
      background: linear-gradient(90deg, var(--gold), transparent);
    }}
    .ornament-diamond {{
      width: 6px;
      height: 6px;
      background: var(--gold);
      transform: rotate(45deg);
    }}

    h1 {{
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(3.5rem, 10vw, 5.5rem);
      font-weight: 300;
      letter-spacing: 0.12em;
      color: var(--ink);
      line-height: 1;
      margin-bottom: 1.2rem;
      opacity: 0;
      animation: fade 0.6s ease 0.35s forwards;
    }}

    .subtitle {{
      font-size: 0.78rem;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--muted);
      font-weight: 300;
      margin-bottom: 3rem;
      opacity: 0;
      animation: fade 0.6s ease 0.5s forwards;
    }}

    a {{
      display: inline-block;
      font-family: 'Lato', sans-serif;
      font-size: 0.72rem;
      font-weight: 400;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      text-decoration: none;
      color: var(--cream);
      background: var(--ink);
      padding: 0.85rem 2.4rem;
      position: relative;
      overflow: hidden;
      transition: color 0.3s ease;
      opacity: 0;
      animation: fade 0.6s ease 0.7s forwards;
    }}

    a::after {{
      content: '';
      position: absolute;
      inset: 0;
      background: var(--gold);
      transform: translateX(-101%);
      transition: transform 0.35s cubic-bezier(0.76, 0, 0.24, 1);
      z-index: -1;
    }}

    a:hover {{ color: var(--ink); }}
    a:hover::after {{ transform: translateX(0); }}

    @keyframes rise {{
      from {{ opacity: 0; transform: translateY(24px); }}
      to   {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes fade {{
      to {{ opacity: 1; }}
    }}
    @keyframes corners {{
      from {{ width: 0; height: 0; opacity: 0; }}
      to   {{ width: 40px; height: 40px; opacity: 0.6; }}
    }}
  </style>
</head>
<body>
  <div class="card">
    <div class="ornament">
      <span class="ornament-line"></span>
      <span class="ornament-diamond"></span>
      <span class="ornament-line"></span>
    </div>
    <h1>Thanks</h1>
    <p class="subtitle">Your response has been received</p>
    <a href="/survey">Submit Another Response</a>
  </div>
</body>
</html>
"""


if __name__ == '__main__':  # Script executed directly?
    app.run(debug=True)  # Launch built-in web server and run this Flask webapp
