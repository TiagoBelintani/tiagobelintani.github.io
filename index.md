# Clone o repositório
git clone https://github.com/tiagobelintani/tiagobelintani.github.io
cd tiagobelintani.github.io

# Crie o index.html com o conteúdo abaixo
cat << 'EOF' > index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tiago Belintani</title>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Open+Sans&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Open Sans', sans-serif;
      color: #222;
      background-color: #fff;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
    h1, h2, h3 {
      font-family: 'Montserrat', sans-serif;
      color: #000;
    }
    h1 {
      font-size: 3em;
      text-align: center;
      margin-bottom: 0;
    }
    h3 {
      font-size: 1.5em;
      text-align: center;
      font-weight: normal;
      margin-top: 0;
    }
    .section {
      background-color: #f7f7f7;
      padding: 20px;
      margin: 20px 0;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .photo {
      text-align: center;
      margin-bottom: 20px;
    }
    .photo img {
      width: 250px;
      border-radius: 10px;
    }
    a {
      color: #000;
      text-decoration: none;
      font-weight: bold;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

  <div class="photo">
    <img src="https://github.com/user-attachments/assets/9545d94c-9f51-457d-8f73-030d5f1ce21f" alt="Tiago Belintani">
  </div>

  <h1>Tiago Belintani</h1>
  <h3>Researcher | Postdoctoral Fellow | Evolutionary Scientist – Brazil</h3>

  <p>Hello, I'm <strong>Tiago Belintani</strong>, a postdoctoral researcher at <strong>UNESP</strong>. I study <strong>evolution</strong>, <strong>phylogenomics</strong>, and <strong>systematics</strong> of <em>Triatominae</em> (vectors of Chagas disease) and <em>Theraphosidae</em> (tarantulas). My background is in <strong>Animal Biology</strong>, with strong emphasis on <strong>bioinformatics</strong>, <strong>evolutionary biology</strong>, and <strong>morphometric analysis</strong>.</p>

  <div class="section">
    <h2>🧬 Work</h2>
    <p>Researcher in Evolutionary Biology</p>
    <p>Bioinformatician for Transcriptomic and Phylogenomic Projects</p>
  </div>

  <div class="section">
    <h2>🎓 Education</h2>
    <ul>
      <li><strong>Universidade Estadual de Campinas</strong> – IB/Unicamp</li>
      <li><strong>Faculdade de Ciências Farmacêuticas – FCFAR/Unesp</strong></li>
      <li><strong>University of Idaho</strong> – UIDAHO</li>
      <li><strong>São Paulo State University (Unesp)</strong> – Campus de Rio Claro</li>
    </ul>
  </div>

  <div class="section">
    <h2>🧠 Descrição</h2>
    <blockquote>
      Currently using computational tools, I research: transcriptome, phylogeny, morphology, and <em>Triatominae</em> morphometry.<br>
      — <em>Tiago B.</em>
    </blockquote>
    <p>🔗 <a href="https://www2.fcfar.unesp.br/#!/triatominae" target="_blank">Coleção de Triatominae FCFAR - Unesp Araraquara</a></p>
  </div>

  <div class="section">
    <h2>📬 Contact Me</h2>
    <p><strong>Email:</strong> <a href="mailto:tiagobellintani@gmail.com">tiagobellintani@gmail.com</a></p>
    <p><strong>GitHub:</strong> <a href="https://github.com/TiagoBelintani">github.com/TiagoBelintani</a></p>
  </div>

  <div class="section">
    <h2>📄 Academic Profiles</h2>
    <p><a href="https://scholar.google.com/citations?user=Ah8QjuIAAAAJ&hl=pt-BR">Google Scholar</a></p>
    <p><a href="https://www.researchgate.net/profile/Tiago-Belintani?ev=hdr_xprf">ResearchGate</a></p>
    <p><a href="https://lattes.cnpq.br/8948388411348223">Lattes</a></p>
  </div>

</body>
</html>
EOF

# Git commit e push
git add index.html
git commit -m "Create GitHub Pages with personal site"
git push origin main


