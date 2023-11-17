# Mafatih Admin
<br>
<h2>How to Run? </h2>
<br>

<h3>
  create a new virtual environment and activate it.
</h3>
<br>

<h2>
  install the dependencies:
</h2>
<div class="highlight highlight-source-shell">
  <pre>$ pip install -r requirements.txt</pre>
</div>
<br>

<h2>
  create and migrate the database:
</h2>
<div class="highlight highlight-source-shell">
  <pre>$ python manage.py migrate</pre>
</div>
<br>

<h2>
  run the server:
</h2>
<div class="highlight highlight-source-shell">
  <pre>$ python manage.py runserver</pre>
</div>
<br>

<br>
<h2>How to Run in docker? </h2>
<br>
<h3>
  install docker in your machine
</h3>
<br>

<h2>
  in the project directory run this command to create an docker image:
</h2>
<div class="highlight highlight-source-shell">
  <pre>$ docker build -t [choose a name] . </pre>
</div>
<br>
<h2>
  run the image in an intractive mod
</h2>
<div class="highlight highlight-source-shell">
  <pre>$ docker run -it -p 80:80 [the name you chose]</pre>
</div>
<br>
to open the project  user is +989120787285 and the pass is 152490
the projects database is mysql but i commented those lines in settings.py in this demo


the user is +0989120787285 and the pass is 152490

