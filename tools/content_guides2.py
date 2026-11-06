"""Extra guides: terry vs T-shirt, storing/washing rags, Québec rag glossary, budget calculator."""
BAG, SHOP, TEXT = "sac-chiffons-t-shirt-couleur-25-lb.webp", "sac-de-chiffons-d-atelier-conditionnes-prets-a-l-u.webp", "textiles-de-coton-recuperes.webp"
P = {}

P["guide-ratine"] = {"kind": "guide", "img": BAG, "rel": ["couleur", "blancs", "garage"],
 "fr": {"path": "/guides/ratine-ou-t-shirt/", "short": "Ratine ou t-shirt : quel chiffon choisir",
  "title": "Chiffons ratine ou t-shirt : lequel choisir?",
  "desc": "Ratine (tissu éponge) ou jersey de t-shirt, blanc ou couleur : comparaison de l'absorption, de la douceur et des usages pour choisir le bon chiffon d'essuyage.",
  "eyebrow": "Guide · choisir", "h1": "Ratine ou t-shirt : quel chiffon d'essuyage choisir?",
  "lede": "Les deux sont en coton recyclé et coûtent le même prix en couleur. La différence : l'épaisseur et l'usage.",
  "card": "Absorption, douceur, usages : le comparatif pour bien choisir.", "alt": "Sac de chiffons t-shirt couleur",
  "body": """<h2>La ratine (tissu éponge)</h2>
<p>La ratine vient de serviettes et de draps de bain. Elle est épaisse, bouclée et retient beaucoup de liquide. C'est le choix pour l'huile, la graisse, l'eau et les gros dégâts.</p>
<h2>Le t-shirt (jersey)</h2>
<p>Le jersey vient de t-shirts et de vêtements en coton tricoté. Il est mince, doux et souple, et laisse peu de peluches. C'est le chiffon tout usage : mains, outils, surfaces, nettoyage courant.</p>
<h2>Comparatif</h2>
<table><thead><tr><th></th><th>Ratine</th><th>T-shirt</th></tr></thead><tbody>
<tr><td>Épaisseur</td><td>Épaisse</td><td>Mince</td></tr>
<tr><td>Absorption</td><td>Très élevée</td><td>Bonne</td></tr>
<tr><td>Douceur</td><td>Moyenne</td><td>Élevée</td></tr>
<tr><td>Idéal pour</td><td>Huile, graisse, eau, déversements</td><td>Mains, outils, surfaces, polissage</td></tr></tbody></table>
<h2>Blanc ou couleur?</h2>
<p>La <a href="{{couleur}}">couleur</a> (32 $ le [pack]) convient à presque tout. Le <a href="{{blancs}}">blanc</a> (42 $) ne laisse pas de teinture : prenez-le pour la peinture, la teinture du bois, le vernis et les surfaces pâles.</p>""",
  "faq": [("La ratine laisse-t-elle plus de peluches?", "Un peu plus que le t-shirt, à cause de ses boucles. Pour les surfaces délicates, choisissez le t-shirt blanc."),
          ("Peut-on mélanger ratine et t-shirt dans une commande?", "Oui. Chaque [pack] contient un seul produit, mais vous pouvez commander plusieurs produits ensemble.")]},
 "en": {"path": "/en/guides/terry-vs-t-shirt-rags/", "short": "Terry vs T-shirt: which rag to choose",
  "title": "Terry vs T-shirt rags: which should you choose?",
  "desc": "Terry (towel cloth) or T-shirt jersey, white or colored: absorbency, softness and best uses compared, to choose the right wiping rag.",
  "eyebrow": "Guide · choosing", "h1": "Terry vs T-shirt: which wiping rag should you choose?",
  "lede": "Both are recycled cotton and cost the same in colored. The difference is thickness and use.",
  "card": "Absorbency, softness, uses: the comparison to choose well.", "alt": "Bag of colored T-shirt rags",
  "body": """<h2>Terry (towel cloth)</h2>
<p>Terry comes from bath towels and sheets. It's thick, looped and holds a lot of liquid. It's the pick for oil, grease, water and big spills.</p>
<h2>T-shirt (jersey)</h2>
<p>Jersey comes from T-shirts and knitted cotton clothing. It's thin, soft and flexible, and low-lint. It's the all-purpose rag: hands, tools, surfaces, everyday cleaning.</p>
<h2>Comparison</h2>
<table><thead><tr><th></th><th>Terry</th><th>T-shirt</th></tr></thead><tbody>
<tr><td>Thickness</td><td>Thick</td><td>Thin</td></tr>
<tr><td>Absorbency</td><td>Very high</td><td>Good</td></tr>
<tr><td>Softness</td><td>Medium</td><td>High</td></tr>
<tr><td>Best for</td><td>Oil, grease, water, spills</td><td>Hands, tools, surfaces, polishing</td></tr></tbody></table>
<h2>White or colored?</h2>
<p><a href="{{couleur}}">Colored</a> ($32 per [pack]) handles almost everything. <a href="{{blancs}}">White</a> ($42) leaves no dye: use it for paint, wood stain, varnish and light-colored surfaces.</p>""",
  "faq": [("Does terry leave more lint?", "A little more than T-shirt, because of its loops. For delicate surfaces, choose white T-shirt rags."),
          ("Can I mix terry and T-shirt in one order?", "Yes. Each [pack] holds one product, but you can order several products together.")]}}

P["guide-ranger"] = {"kind": "guide", "img": SHOP, "rel": ["guide-huileux", "garage", "marine"],
 "fr": {"path": "/guides/ranger-laver-reutiliser-chiffons/", "short": "Ranger, laver et jeter ses chiffons",
  "title": "Comment ranger, laver, réutiliser et jeter ses chiffons",
  "desc": "Ranger les chiffons propres et souillés, les laver sans perdre leur absorption, savoir quand les jeter et où les apporter au Québec (écocentre, collecte).",
  "eyebrow": "Guide · entretien", "h1": "Ranger, laver, réutiliser et jeter ses chiffons",
  "lede": "Bien rangés et bien lavés, vos chiffons durent plus longtemps. Bien jetés, ils ne causent ni incendie ni pollution.",
  "card": "Rangement, lavage sans assouplissant, et où jeter les chiffons souillés.", "alt": "Chiffons d'atelier rangés",
  "body": """<h2>Ranger les chiffons propres</h2>
<p>Gardez-les dans leur sac fermé ou un bac à couvercle, au sec, loin de la poussière et des produits chimiques. Un bac par poste de travail évite le gaspillage.</p>
<h2>Ranger les chiffons souillés</h2>
<p>Les chiffons imbibés d'huile, de solvant, de teinture ou de carburant vont dans un <b>contenant métallique fermé</b>, jamais en tas. Videz-le chaque jour. Pourquoi : voir <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p>
<h2>Laver et réutiliser</h2>
<ul><li>Lavez seulement les chiffons <b>légèrement sales</b> : eau, poussière, produits ménagers doux.</li>
<li>Lavez-les à part, à l'eau chaude.</li>
<li><b>Pas d'assouplissant</b> : il réduit l'absorption du coton.</li>
<li>Ne mettez jamais à la sécheuse un chiffon qui a contenu de l'huile ou du solvant.</li></ul>
<h2>Quand et où les jeter</h2>
<p>Un chiffon déchiré ou imbibé d'un produit dangereux doit être jeté. Les chiffons contaminés par de la peinture, des solvants ou des huiles sont des résidus dangereux : les particuliers les apportent à un écocentre, et les entreprises passent par une entreprise de collecte spécialisée. Vérifiez les règles de votre municipalité.</p>""",
  "faq": [("Pourquoi éviter l'assouplissant?", "Il dépose une couche sur les fibres qui empêche le coton d'absorber. Vos chiffons essuieraient moins bien."),
          ("Un chiffon de ménage peut-il aller à la poubelle?", "Oui, s'il n'a servi qu'avec de l'eau ou des produits ménagers doux. S'il contient un produit dangereux, suivez les consignes de votre municipalité.")]},
 "en": {"path": "/en/guides/store-wash-reuse-rags/", "short": "Storing, washing and disposing of rags",
  "title": "How to store, wash, reuse and dispose of rags",
  "desc": "How to store clean and dirty rags, wash them without losing absorbency, know when to toss them and where to take them in Québec (ecocentre, special pickup).",
  "eyebrow": "Guide · care", "h1": "Storing, washing, reusing and disposing of rags",
  "lede": "Stored and washed well, your rags last longer. Disposed of well, they cause neither fires nor pollution.",
  "card": "Storage, washing without softener, and where to dispose of dirty rags.", "alt": "Stored shop rags",
  "body": """<h2>Storing clean rags</h2>
<p>Keep them in their closed bag or a lidded bin, dry, away from dust and chemicals. One bin per workstation avoids waste.</p>
<h2>Storing dirty rags</h2>
<p>Rags soaked with oil, solvent, stain or fuel go in a <b>closed metal container</b>, never in a pile. Empty it daily. Why: see <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p>
<h2>Washing and reusing</h2>
<ul><li>Only wash <b>lightly soiled</b> rags: water, dust, mild cleaning products.</li>
<li>Wash them separately, in hot water.</li>
<li><b>No fabric softener</b>: it reduces cotton's absorbency.</li>
<li>Never put a rag that held oil or solvent in a dryer.</li></ul>
<h2>When and where to dispose of them</h2>
<p>A torn rag, or one soaked with a hazardous product, should be thrown out. Rags contaminated with paint, solvents or oils are hazardous waste: households take them to an ecocentre, and businesses use a specialized waste pickup company. Check your municipality's rules.</p>""",
  "faq": [("Why avoid fabric softener?", "It coats the fibers and stops cotton from absorbing, so your rags wipe less well."),
          ("Can a cleaning rag go in the trash?", "Yes, if it was only used with water or mild cleaning products. If it holds a hazardous product, follow your municipality's rules.")]}}

P["glossaire"] = {"kind": "guide", "img": TEXT, "rel": ["guide-ratine", "couleur", "faq"],
 "fr": {"path": "/guides/guenille-chiffon-torchon-lexique/", "short": "Guenille, chiffon, linge : le lexique",
  "title": "Guenille, chiffon, linge, ratine : le lexique québécois",
  "desc": "Guenille, chiffon d'essuyage, linge, torchon, ratine, jersey : le vocabulaire québécois et anglais des chiffons, pour bien chercher et bien commander.",
  "eyebrow": "Guide · lexique", "h1": "Guenille, chiffon, linge, ratine : le lexique des chiffons",
  "lede": "Au Québec, on dit guenille, chiffon ou linge. En anglais, rag, wiper ou shop rag. Voici ce que chaque mot veut dire.",
  "card": "Le vocabulaire québécois et anglais des chiffons, mot par mot.", "alt": "Textiles de coton récupérés",
  "body": "<p>Les mots changent d'une région et d'un métier à l'autre. Ce lexique vous aide à comparer les offres et à commander le bon produit.</p>",
  "terms": [("Guenille", "Mot québécois pour un chiffon fait d'un vieux tissu, utilisé pour nettoyer ou essuyer. « Des guenilles » se vendent souvent au poids, en sac."),
            ("Chiffon d'essuyage", "Terme général pour un morceau de tissu servant à essuyer : huile, graisse, liquides, poussière. En anglais : wiping rag ou wiper."),
            ("Chiffon d'atelier", "Chiffon utilisé dans les garages et ateliers. En anglais : shop rag."),
            ("Linge", "Au Québec, « un linge » désigne aussi un chiffon ou une serviette de nettoyage, comme dans « linge à vaisselle »."),
            ("Torchon", "Mot plus courant en France qu'au Québec pour un chiffon de nettoyage ou un linge à vaisselle."),
            ("Ratine", "Au Québec, le tissu éponge bouclé des serviettes. Épais et très absorbant. En anglais : terry."),
            ("Jersey (t-shirt)", "Tissu de coton tricoté des t-shirts. Mince, doux et peu pelucheux."),
            ("Peu pelucheux", "Qui laisse peu de fibres sur la surface. En anglais : low-lint."),
            ("Sans transfert de couleur", "Chiffon blanc qui ne laisse pas de teinture sur la surface essuyée."),
            ("Textile post-consommation", "Vêtements et tissus usagés récupérés après usage, puis triés et transformés en chiffons."),
            ("Vendu au poids", "Les chiffons se vendent en livres (lb) plutôt qu'à la pièce, car la taille des morceaux varie."),
            ("Traitement anti-punaises", "Traitement des textiles contre les punaises de lit avant l'emballage.")]},
 "en": {"path": "/en/guides/rag-glossary-quebec/", "short": "Rag glossary: guenille, chiffon, terry",
  "title": "Rag glossary: guenille, chiffon, terry, shop rag",
  "desc": "Guenille, chiffon, linge, ratine, wiper, shop rag: the Québec French and English vocabulary of rags, to search and order with confidence.",
  "eyebrow": "Guide · glossary", "h1": "Rag glossary: Québec French and English terms",
  "lede": "In Québec, people say guenille, chiffon or linge. In English, rag, wiper or shop rag. Here's what each word means.",
  "card": "The Québec French and English rag vocabulary, word by word.", "alt": "Reclaimed cotton textiles",
  "body": "<p>Words change from one region and trade to the next. This glossary helps you compare offers and order the right product.</p>",
  "terms": [("Guenille", "Québec French for a rag made from old fabric, used for cleaning or wiping. Guenilles are often sold by weight, in bags."),
            ("Chiffon d'essuyage (wiping rag)", "General term for a piece of fabric used to wipe oil, grease, liquids or dust. Also called a wiper."),
            ("Shop rag (chiffon d'atelier)", "A rag used in garages and workshops."),
            ("Linge", "In Québec, \"un linge\" also means a cleaning cloth or towel, as in \"linge à vaisselle\" (dish towel)."),
            ("Torchon", "Word used more in France than in Québec for a cleaning rag or dish towel."),
            ("Terry (ratine)", "Looped towel fabric. Thick and highly absorbent. Québec French calls it ratine."),
            ("Jersey (T-shirt)", "Knitted cotton fabric from T-shirts. Thin, soft and low-lint."),
            ("Low-lint (peu pelucheux)", "Leaves few fibers on the surface."),
            ("No color transfer (sans transfert de couleur)", "White rag that leaves no dye on the wiped surface."),
            ("Post-consumer textile", "Used clothing and fabric collected after use, then sorted and turned into rags."),
            ("Sold by weight", "Rags are sold by the pound (lb) rather than by the piece, because piece sizes vary."),
            ("Bedbug treatment (traitement anti-punaises)", "Treating textiles against bedbugs before packing.")]}}

P["calculateur"] = {"kind": "tool", "img": None, "rel": ["gros", "livraison", "guide-ratine"],
 "fr": {"path": "/calculateur-chiffons/", "short": "Calculateur de budget",
  "title": "Calculateur : combien de sacs de chiffons par mois?",
  "desc": "Estimez vos sacs de chiffons de 25 lb par mois et votre budget avant et après taxes (TPS et TVQ), selon votre consommation et le produit choisi.",
  "eyebrow": "Outil · budget", "h1": "Calculateur : combien de sacs de chiffons vous faut-il?",
  "lede": "Entrez votre consommation, choisissez un produit : vous obtenez le nombre de sacs par mois et le budget avant et après taxes.",
  "card": "Nombre de sacs par mois et budget avec TPS et TVQ.",
  "body": """<h2>Comment estimer votre consommation</h2>
<p>Le plus simple : commandez quelques [packs] et notez combien de temps ils durent. Divisez ensuite 25 lb par le nombre de semaines pour obtenir vos livres par semaine.</p>
<h2>Hors Laval et Montréal</h2>
<p>Le minimum est de 1 000 lb par livraison (40 sacs, produits mélangés acceptés). Le calculateur indique combien de mois de consommation cela représente. Voir les <a href="{{livraison}}">conditions de livraison</a>.</p>
<p>Ce calcul est une estimation. Les frais de livraison ne sont pas inclus : ils dépendent de votre adresse et sont indiqués dans la soumission.</p>""",
  "tool": {"lbw": "Consommation (lb par semaine)", "prod": "Produit", "zone": "Livraison", "z1": "Laval ou Montréal", "z2": "Ailleurs au Québec",
           "bags": "Sacs de 25 lb par mois", "pre": "Budget mensuel avant taxes", "tax": "TPS (5 %) + TVQ (9,975 %)", "tot": "Total mensuel avec taxes",
           "min": "Le minimum de 1 000 lb correspond à environ {m} mois de consommation.", "cur": "fr"}},
 "en": {"path": "/en/rag-calculator/", "short": "Budget calculator",
  "title": "Calculator: how many bags of rags per month?",
  "desc": "Estimate your 25 lb bags of rags per month and your budget before and after tax (GST and QST), based on your usage and the product you choose.",
  "eyebrow": "Tool · budget", "h1": "Calculator: how many bags of rags do you need?",
  "lede": "Enter your usage and choose a product: you get the number of bags per month and the budget before and after tax.",
  "card": "Bags per month and budget with GST and QST.",
  "body": """<h2>How to estimate your usage</h2>
<p>The simplest way: order a few [packs] and note how long they last. Then divide 25 lb by the number of weeks to get your pounds per week.</p>
<h2>Outside Laval and Montréal</h2>
<p>The minimum is 1,000 lb per delivery (40 bags, mixed products welcome). The calculator shows how many months of usage that represents. See the <a href="{{livraison}}">delivery terms</a>.</p>
<p>This is an estimate. Delivery fees aren't included: they depend on your address and are shown in the quote.</p>""",
  "tool": {"lbw": "Usage (lb per week)", "prod": "Product", "zone": "Delivery", "z1": "Laval or Montréal", "z2": "Elsewhere in Québec",
           "bags": "25 lb bags per month", "pre": "Monthly budget before tax", "tax": "GST (5%) + QST (9.975%)", "tot": "Monthly total with tax",
           "min": "The 1,000 lb minimum equals about {m} months of usage.", "cur": "en"}}}

P["guide-prix"] = {"kind": "guide", "img": BAG, "rel": ["couleur", "blancs", "gros"],
 "fr": {"path": "/guides/prix-guenilles-laval-montreal/", "short": "Prix des guenilles à Laval et Montréal",
  "title": "Prix des guenilles à Laval et Montréal (2026)",
  "desc": "Prix des guenilles (chiffons recyclés) à Laval et Montréal : 32 $ le sac de 25 lb en couleur, 42 $ en blanc, soit 1,28 $ à 1,68 $ la livre avant taxes.",
  "eyebrow": "Guide · prix", "h1": "Prix des guenilles et chiffons recyclés à Laval et Montréal",
  "lede": "Chiffons ÉCO (Entretien Laval) vend des chiffons recyclés – guenilles en coton à partir de 1,28 $ la livre, en sacs de 25 lb, dans le Grand Montréal.",
  "card": "Prix par sac et par livre, prix en gros, livraison.", "alt": "Sac de chiffons t-shirt couleur de 25 lb",
  "body": """<h2>Nos prix (avant taxes)</h2>
<table><thead><tr><th>Produit</th><th>Prix du [pack] de 25 lb</th><th>Prix par livre</th></tr></thead><tbody>
<tr><td>T-shirt couleur</td><td>32 $</td><td>1,28 $</td></tr>
<tr><td>Ratine couleur</td><td>32 $</td><td>1,28 $</td></tr>
<tr><td>T-shirt blanc</td><td>42 $</td><td>1,68 $</td></tr>
<tr><td>Ratine blanche</td><td>42 $</td><td>1,68 $</td></tr></tbody></table>
<p>À partir de 50 [packs] : 28 $ en couleur et 38 $ en blanc. Voir <a href="{{gros}}">guenilles en gros</a>.</p>
<h2>Le choix le plus économique</h2>
<p>Le <a href="{{couleur}}">chiffon couleur</a> est le moins cher : 32 $ le [pack]. Il convient à l'huile, à la graisse, aux déversements et au nettoyage courant. Prenez le <a href="{{blancs}}">blanc</a> seulement pour la peinture, le vernis, les solvants et les surfaces pâles.</p>
<h2>Ce qui est inclus</h2>
<p>Des chiffons de coton recyclé lavés à l'eau chaude, triés, traités contre les punaises de lit, sans boutons ni fermetures éclair, coupés et prêts à l'emploi. Un seul type de chiffon par [pack].</p>
<h2>Livraison</h2>
<p>Nous livrons à Laval, à Montréal et dans le Grand Montréal. Ailleurs au Québec, à partir de 1 000 lb. Voir les <a href="{{livraison}}">conditions de livraison</a>.</p>""",
  "faq": [("Quelle est la guenille la moins chère à Laval?", "Chez Chiffons ÉCO, la guenille couleur (t-shirt ou ratine) : 32 $ le [pack] de 25 lb, soit 1,28 $ la livre avant taxes, ou 28 $ à partir de 50 [packs]."),
          ("Les taxes sont-elles incluses?", "Non. Les prix sont avant TPS (5 %) et TVQ (9,975 %)."),
          ("Où acheter des chiffons recyclés à Montréal?", "Chiffons ÉCO (Entretien Laval) livre ses chiffons recyclés à Montréal. Écrivez à info@entretienlaval.ca ou remplissez le formulaire de soumission.")]},
 "en": {"path": "/en/guides/rag-prices-laval-montreal/", "short": "Rag prices in Laval and Montréal",
  "title": "Rag prices in Laval and Montréal (2026)",
  "desc": "How much do recycled wiping rags cost in Laval and Montréal? $32 per 25 lb bag for colored, $42 for white: $1.28 to $1.68 per pound before tax.",
  "eyebrow": "Guide · prices", "h1": "Recycled rag prices in Laval and Montréal",
  "lede": "Chiffons ÉCO (Entretien Laval) sells recycled cotton wiping rags from $1.28 per pound, in 25 lb bags, across Greater Montreal.",
  "card": "Price per bag and per pound, wholesale price, delivery.", "alt": "25 lb bag of colored T-shirt rags",
  "body": """<h2>Our prices (before tax)</h2>
<table><thead><tr><th>Product</th><th>Price per 25 lb [pack]</th><th>Price per pound</th></tr></thead><tbody>
<tr><td>Colored T-shirt</td><td>$32</td><td>$1.28</td></tr>
<tr><td>Colored terry</td><td>$32</td><td>$1.28</td></tr>
<tr><td>White T-shirt</td><td>$42</td><td>$1.68</td></tr>
<tr><td>White terry</td><td>$42</td><td>$1.68</td></tr></tbody></table>
<p>From 50 [packs]: $28 colored and $38 white. See <a href="{{gros}}">wholesale rags</a>.</p>
<h2>The cheapest choice</h2>
<p><a href="{{couleur}}">Colored rags</a> cost the least: $32 per [pack]. They handle oil, grease, spills and everyday cleaning. Choose <a href="{{blancs}}">white</a> only for paint, varnish, solvents and light surfaces.</p>
<h2>What's included</h2>
<p>Recycled cotton rags washed in hot water, sorted, treated against bedbugs, free of buttons and zippers, cut and ready to use. One rag type per [pack].</p>
<h2>Delivery</h2>
<p>We deliver in Laval, Montréal and Greater Montreal. Elsewhere in Québec, from 1,000 lb. See the <a href="{{livraison}}">delivery terms</a>.</p>""",
  "faq": [("What are the cheapest rags in Laval?", "At Chiffons ÉCO, colored rags (T-shirt or terry): $32 per 25 lb [pack], $1.28 per pound before tax, or $28 from 50 [packs]."),
          ("Are taxes included?", "No. Prices are before GST (5%) and QST (9.975%)."),
          ("Where can I buy recycled rags in Montréal?", "Chiffons ÉCO (Entretien Laval) delivers recycled rags in Montréal. Email info@entretienlaval.ca or fill in the quote form.")]}}

P["guide-teinture"] = {"kind": "guide", "img": BAG, "rel": ["blancs", "peinture", "guide-huileux"],
 "fr": {"path": "/guides/meilleur-chiffon-teinture-bois/", "short": "Quel chiffon pour teindre le bois",
  "title": "Quel chiffon pour teindre le bois? (teinture, vernis)",
  "desc": "Le meilleur chiffon pour teindre le bois, appliquer un vernis ou une huile : coton blanc, t-shirt peu pelucheux, ratine pour essuyer. Et quoi faire après.",
  "eyebrow": "Guide · peinture et finition", "h1": "Quel chiffon utiliser pour teindre le bois?",
  "lede": "Pour la teinture, le vernis et l'huile, prenez un chiffon de coton blanc : il absorbe bien, ne laisse pas de couleur sur le bois et laisse peu de peluches.",
  "card": "Coton blanc, t-shirt ou ratine : le bon chiffon pour la finition du bois.",
  "alt": "Sacs de chiffons blancs recyclés",
  "body": """<h2>Le chiffon idéal : coton blanc</h2>
<p>Le coton absorbe la teinture et l'huile, contrairement aux tissus synthétiques qui les étalent. Le <a href="{{blancs}}">chiffon blanc</a> ne transfère aucune couleur sur le bois, même avec des solvants. C'est le choix sûr pour les teintures pâles, le vernis et les surfaces claires.</p>
<h2>T-shirt ou ratine?</h2>
<table><thead><tr><th>Étape</th><th>Chiffon conseillé</th><th>Pourquoi</th></tr></thead><tbody>
<tr><td>Appliquer la teinture ou l'huile</td><td>T-shirt blanc</td><td>Mince, souple, peu pelucheux</td></tr>
<tr><td>Essuyer l'excédent</td><td>Ratine blanche</td><td>Épaisse, retient beaucoup de liquide</td></tr>
<tr><td>Polir entre les couches</td><td>T-shirt blanc</td><td>Doux, laisse une surface lisse</td></tr>
<tr><td>Nettoyer les outils et les mains</td><td>Couleur</td><td>Moins cher, la couleur n'a pas d'importance</td></tr></tbody></table>
<h2>Après usage : attention au feu</h2>
<p>Les chiffons imbibés d'huile de lin, de teinture à l'huile ou de vernis peuvent s'enflammer seuls en séchant. Ne les laissez jamais en boule. Voir <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p>
<h2>Prix</h2>
<p>Chiffons blancs : 42 $ le [pack] de 25 lb, avant taxes (38 $ à partir de 50 [packs]). Voir aussi les <a href="{{peinture}}">chiffons pour la peinture et la finition</a>.</p>""",
  "faq": [("Quel est le meilleur chiffon pour teindre le bois?", "Un chiffon de coton blanc, propre et sans peluches. Le t-shirt blanc pour appliquer, la ratine blanche pour essuyer l'excédent."),
          ("Peut-on utiliser des chiffons de couleur pour la teinture?", "Pour nettoyer les outils, oui. Pour appliquer la teinture ou le vernis, prenez du blanc : les solvants peuvent faire déteindre un tissu coloré sur le bois."),
          ("Que faire des chiffons imbibés de teinture à l'huile?", "Étalez-les à plat dehors pour sécher, ou mettez-les dans un contenant de métal fermé rempli d'eau. Ne les jetez pas en boule.")]},
 "en": {"path": "/en/guides/best-rag-for-staining-wood/", "short": "Best rag for staining wood",
  "title": "Best rag for staining wood (stain, varnish, oil)",
  "desc": "The best rag for staining wood, varnish and finishing oil: white cotton, low-lint T-shirt to apply, terry to wipe off. Plus what to do with used rags.",
  "eyebrow": "Guide · painting and finishing", "h1": "What kind of rag should you use for staining wood?",
  "lede": "For stain, varnish and oil, use a white cotton rag: it absorbs well, leaves no dye on the wood and is low-lint.",
  "card": "White cotton, T-shirt or terry: the right rag for wood finishing.",
  "alt": "Bags of white recycled rags",
  "body": """<h2>The best rag: white cotton</h2>
<p>Cotton soaks up stain and oil, while synthetic fabrics just spread them around. A <a href="{{blancs}}">white rag</a> transfers no color to the wood, even with solvents. It's the safe pick for light stains, varnish and pale surfaces.</p>
<h2>T-shirt or terry?</h2>
<table><thead><tr><th>Step</th><th>Recommended rag</th><th>Why</th></tr></thead><tbody>
<tr><td>Applying stain or oil</td><td>White T-shirt</td><td>Thin, flexible, low-lint</td></tr>
<tr><td>Wiping off the excess</td><td>White terry</td><td>Thick, holds a lot of liquid</td></tr>
<tr><td>Buffing between coats</td><td>White T-shirt</td><td>Soft, leaves a smooth surface</td></tr>
<tr><td>Cleaning tools and hands</td><td>Colored</td><td>Cheaper, color doesn't matter</td></tr></tbody></table>
<h2>After use: fire risk</h2>
<p>Rags soaked in linseed oil, oil-based stain or varnish can catch fire on their own as they dry. Never leave them balled up. See <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p>
<h2>Price</h2>
<p>White rags: $42 per 25 lb [pack], before tax ($38 from 50 [packs]). See also <a href="{{peinture}}">rags for painting and finishing</a>.</p>""",
  "faq": [("What is the best rag for staining wood?", "A clean, lint-free white cotton rag. White T-shirt to apply, white terry to wipe off the excess."),
          ("Can I use colored rags for staining?", "For cleaning tools, yes. To apply stain or varnish, use white: solvents can make a colored fabric bleed onto the wood."),
          ("How do I dispose of oil-based stain rags?", "Lay them flat outdoors to dry, or put them in a closed metal container filled with water. Never throw them out balled up.")]}}

P["guide-industriel"] = {"kind": "guide", "img": SHOP, "rel": ["usinage", "garage", "industrie"],
 "fr": {"path": "/guides/chiffons-industriels-guide-achat/", "short": "Chiffons industriels : guide d'achat",
  "title": "Chiffons industriels : guide d'achat pour ateliers",
  "desc": "Chiffons industriels et d'atelier : ratine ou t-shirt, blanc ou couleur, quantité par mois et prix au Québec. Pour usines, garages et ateliers.",
  "eyebrow": "Guide · industrie", "h1": "Chiffons industriels : comment bien choisir",
  "lede": "Usinage, mécanique, imprimerie, entretien : le bon chiffon industriel dépend de ce que vous essuyez. Voici comment choisir et combien prévoir.",
  "card": "Le bon chiffon d'atelier selon l'usage, la quantité et le prix.",
  "alt": "Sac de chiffons d'atelier prêts à l'emploi",
  "body": """<h2>Selon ce que vous essuyez</h2>
<table><thead><tr><th>Usage</th><th>Chiffon conseillé</th></tr></thead><tbody>
<tr><td>Huile de coupe, graisse, copeaux (<a href="{{usinage}}">usinage, CNC</a>)</td><td>Ratine couleur</td></tr>
<tr><td>Mains, outils, pièces (<a href="{{garage}}">garages, mécanique</a>)</td><td>T-shirt couleur</td></tr>
<tr><td>Encre, solvants (<a href="{{industrie}}">imprimeries, usines</a>)</td><td>T-shirt blanc</td></tr>
<tr><td>Peinture, vernis, surfaces pâles</td><td>Blanc (t-shirt ou ratine)</td></tr>
<tr><td>Déversements, eau</td><td>Ratine couleur</td></tr></tbody></table>
<h2>Ce qu'un chiffon industriel doit être</h2>
<p>Sans métal, boutons ni fermetures éclair, pour ne pas rayer les pièces ni les machines. Lavé, trié et coupé, prêt à l'emploi. Nos chiffons recyclés sont lavés à l'eau chaude et traités contre les punaises de lit, un seul type par [pack].</p>
<h2>Combien en prévoir?</h2>
<p>Utilisez le <a href="{{calculateur}}">calculateur de chiffons</a> pour estimer votre consommation par mois selon votre secteur et votre équipe.</p>
<h2>Prix (avant taxes)</h2>
<p>[pack] de 25 lb : 32 $ en couleur, 42 $ en blanc. À partir de 50 [packs] : 28 $ et 38 $. Voir <a href="{{gros}}">guenilles en gros</a>.</p>""",
  "faq": [("Où acheter des chiffons industriels pas chers à Laval?", "Chez Chiffons ÉCO (Entretien Laval), 1355 boul. Le Corbusier, Laval : chiffons recyclés – guenilles couleur à 32 $ le [pack] de 25 lb (1,28 $/lb), blancs à 42 $, ou 28 $ / 38 $ dès 50 [packs], avant taxes. Ramassage à Laval ou livraison à Laval (15 $) et Montréal (25 $, dès 2 [packs])."),
  ("Quelle est la différence entre chiffon industriel et chiffon d'atelier?", "Aucune en pratique : les deux désignent des chiffons de coton recyclé pour essuyer l'huile, la graisse et les solvants en usine, en garage ou en atelier."),
          ("Quel chiffon pour un atelier d'usinage?", "La ratine couleur : épaisse et absorbante pour l'huile de coupe. Nos chiffons n'ont ni métal ni boutons qui pourraient rayer les pièces."),
          ("Livrez-vous les chiffons industriels?", "Oui, à Laval (15 $, dès 1 [pack]), à Montréal (25 $, dès 2 [packs]) et ailleurs au Québec à partir de 1 000 lb.")]},
 "en": {"path": "/en/guides/industrial-shop-rags-buying-guide/", "short": "Industrial shop rags: buying guide",
  "title": "Industrial shop rags: a buying guide for shops",
  "desc": "Industrial and shop rags: terry or T-shirt, white or colored, how many per month and prices in Québec. The guide for plants, garages and machine shops.",
  "eyebrow": "Guide · industry", "h1": "Industrial shop rags: how to choose",
  "lede": "Machining, mechanics, printing, maintenance: the right industrial rag depends on what you wipe. Here's how to choose and how many to plan for.",
  "card": "The right shop rag by use, quantity and price.",
  "alt": "Bag of ready-to-use shop rags",
  "body": """<h2>By what you wipe</h2>
<table><thead><tr><th>Use</th><th>Recommended rag</th></tr></thead><tbody>
<tr><td>Cutting oil, grease, chips (<a href="{{usinage}}">machining, CNC</a>)</td><td>Colored terry</td></tr>
<tr><td>Hands, tools, parts (<a href="{{garage}}">garages, mechanics</a>)</td><td>Colored T-shirt</td></tr>
<tr><td>Ink, solvents (<a href="{{industrie}}">print shops, plants</a>)</td><td>White T-shirt</td></tr>
<tr><td>Paint, varnish, light surfaces</td><td>White (T-shirt or terry)</td></tr>
<tr><td>Spills, water</td><td>Colored terry</td></tr></tbody></table>
<h2>What an industrial rag must be</h2>
<p>No metal, buttons or zippers, so nothing scratches parts or machines. Washed, sorted and cut, ready to use. Our recycled rags are hot-water washed and treated against bed bugs, one type per [pack].</p>
<h2>How many do you need?</h2>
<p>Use the <a href="{{calculateur}}">rag calculator</a> to estimate your monthly use by sector and team size.</p>
<h2>Prices (before tax)</h2>
<p>25 lb [pack]: $32 colored, $42 white. From 50 [packs]: $28 and $38. See <a href="{{gros}}">bulk rags</a>.</p>""",
  "faq": [("Where can I buy cheap industrial rags in Laval?", "At Chiffons ÉCO (Entretien Laval), 1355 boul. Le Corbusier, Laval: colored recycled rags at $32 per 25 lb [pack] ($1.28/lb), white at $42, or $28 / $38 from 50 [packs], before tax. Pickup in Laval or delivery in Laval ($15) and Montréal ($25, from 2 [packs])."),
  ("What's the difference between industrial rags and shop rags?", "None in practice: both are recycled cotton rags for wiping oil, grease and solvents in plants, garages and shops."),
          ("Which rag is best for a machine shop?", "Colored terry: thick and absorbent for cutting oil. Our rags have no metal or buttons that could scratch parts."),
          ("Do you deliver industrial rags?", "Yes: Laval ($15, from 1 [pack]), Montréal ($25, from 2 [packs]) and elsewhere in Québec from 1,000 lb.")]}}

P["guide-metal"] = {"kind": "guide", "img": SHOP, "rel": ["usinage", "soudure", "guide-industriel"],
 "fr": {"path": "/guides/chiffons-atelier-metal-laval-montreal/", "short": "Chiffons pour ateliers de métal à Laval et Montréal",
  "title": "Chiffons pour ateliers d'usinage et de métal à Laval et Montréal",
  "desc": "Où acheter des chiffons pour un atelier d'usinage CNC, de soudure ou de fabrication métallique à Laval et Montréal : produits, prix, ramassage et livraison.",
  "eyebrow": "Guide · usinage · soudure · métal", "h1": "Chiffons pour ateliers d'usinage et de métal à Laval et Montréal",
  "lede": "Ateliers CNC, soudure, fabrication métallique : quel chiffon prendre, combien il coûte et comment l'obtenir rapidement dans le Grand Montréal.",
  "card": "Usinage CNC, soudure, fabrication : produits, prix et livraison à Laval et Montréal.",
  "alt": "Sac de chiffons d'atelier pour usinage et fabrication métallique",
  "body": """<h2>Le bon chiffon selon le travail</h2>
<table><thead><tr><th>Travail</th><th>Chiffon conseillé</th><th>Prix (sac de 25 lb, avant taxes)</th></tr></thead><tbody>
<tr><td>Huile de coupe, liquide de refroidissement, déversements</td><td>Ratine couleur ou ratine blanche</td><td>32 $ / 42 $</td></tr>
<tr><td>Pièces finies, mesure, inspection</td><td>T-shirt blanc</td><td>42 $</td></tr>
<tr><td>Dégraissage avant soudure ou peinture</td><td>T-shirt blanc</td><td>42 $</td></tr>
<tr><td>Mains, outils, établis, entretien des machines</td><td>T-shirt couleur</td><td>32 $</td></tr></tbody></table>
<p>La ratine blanche absorbe autant que la ratine couleur, sans transfert de teinture : un bon choix pour l'huile de coupe sur des pièces finies. Tous nos chiffons sont sans boutons, fermetures éclair ni métal.</p>
<h2>Ramassage et livraison</h2>
<ul><li><b>Ramassage à Laval</b> : 1355 boul. Le Corbusier.</li>
<li><b>Livraison à Laval</b> : 15 $, dès 1 [pack].</li>
<li><b>Livraison à Montréal</b> : 25 $, dès 2 [packs].</li>
<li><b>Ailleurs au Québec</b> : à partir de 1 000 lb (40 [packs]).</li></ul>
<h2>Prix de volume</h2>
<p>À partir de 50 [packs] : 28 $ en couleur et 38 $ en blanc, avant taxes. Facture avec TPS et TVQ. Voir <a href="{{gros}}">guenilles en gros</a> et le <a href="{{calculateur}}">calculateur</a> pour estimer vos besoins par mois.</p>
<h2>Pages par métier</h2>
<p><a href="{{usinage}}">Ateliers d'usinage</a> · <a href="{{soudure}}">Soudure et fabrication métallique</a> · <a href="{{guide-industriel}}">Guide d'achat des chiffons industriels</a></p>""",
  "faq": [("Où acheter des chiffons pour un atelier d'usinage CNC à Montréal?", "Chez Chiffons ÉCO (Entretien Laval), 1355 boul. Le Corbusier, Laval : ratine ou t-shirt, couleur à 32 $ ou blanc à 42 $ le [pack] de 25 lb, avant taxes. Livraison à Montréal 25 $ dès 2 [packs], ou ramassage à Laval."),
          ("Quel est le chiffon le moins cher pour un atelier de métal à Laval?", "Le [pack] de 25 lb en couleur à 32 $ avant taxes (1,28 $/lb), ou 28 $ dès 50 [packs]. Livraison à Laval 15 $ dès 1 [pack]."),
          ("Quel chiffon pour l'huile de coupe?", "La ratine : épaisse et très absorbante. Prenez la ratine blanche (42 $) si vous ne voulez aucun transfert de teinture sur les pièces, sinon la ratine couleur (32 $).")]},
 "en": {"path": "/en/guides/metal-shop-rags-laval-montreal/", "short": "Rags for metal shops in Laval and Montréal",
  "title": "Rags for machine and metal shops in Laval and Montréal",
  "desc": "Where to buy rags for a CNC machine shop, welding or metal fabrication shop in Laval and Montréal: products, prices, pickup and delivery.",
  "eyebrow": "Guide · machining · welding · metal", "h1": "Rags for machine and metal shops in Laval and Montréal",
  "lede": "CNC shops, welding, metal fabrication: which rag to use, what it costs and how to get it fast in Greater Montréal.",
  "card": "CNC machining, welding, fabrication: products, prices and delivery in Laval and Montréal.",
  "alt": "Bag of shop rags for machining and metal fabrication",
  "body": """<h2>The right rag for the job</h2>
<table><thead><tr><th>Job</th><th>Recommended rag</th><th>Price (25 lb bag, before tax)</th></tr></thead><tbody>
<tr><td>Cutting oil, coolant, spills</td><td>Colored terry or white terry</td><td>$32 / $42</td></tr>
<tr><td>Finished parts, measuring, inspection</td><td>White T-shirt</td><td>$42</td></tr>
<tr><td>Degreasing before welding or painting</td><td>White T-shirt</td><td>$42</td></tr>
<tr><td>Hands, tools, benches, machine maintenance</td><td>Colored T-shirt</td><td>$32</td></tr></tbody></table>
<p>White terry absorbs as much as colored terry, with no dye transfer: a good choice for cutting oil on finished parts. All our rags are free of buttons, zippers and metal.</p>
<h2>Pickup and delivery</h2>
<ul><li><b>Pickup in Laval</b>: 1355 boul. Le Corbusier.</li>
<li><b>Delivery in Laval</b>: $15, from 1 [pack].</li>
<li><b>Delivery in Montréal</b>: $25, from 2 [packs].</li>
<li><b>Elsewhere in Québec</b>: from 1,000 lb (40 [packs]).</li></ul>
<h2>Volume pricing</h2>
<p>From 50 [packs]: $28 colored and $38 white, before tax. Invoice with GST and QST. See <a href="{{gros}}">wholesale rags</a> and the <a href="{{calculateur}}">calculator</a> to estimate your monthly needs.</p>
<h2>Pages by trade</h2>
<p><a href="{{usinage}}">Machine shops</a> · <a href="{{soudure}}">Welding and metal fabrication</a> · <a href="{{guide-industriel}}">Industrial shop rags buying guide</a></p>""",
  "faq": [("Where can I buy rags for a CNC machine shop in Montréal?", "From Chiffons ÉCO (Entretien Laval), 1355 boul. Le Corbusier, Laval: terry or T-shirt, $32 colored or $42 white per 25 lb [pack], before tax. Delivery in Montréal $25 from 2 [packs], or pickup in Laval."),
          ("What is the cheapest rag for a metal shop in Laval?", "The 25 lb colored [pack] at $32 before tax ($1.28/lb), or $28 from 50 [packs]. Delivery in Laval $15 from 1 [pack]."),
          ("Which rag is best for cutting oil?", "Terry: thick and very absorbent. Choose white terry ($42) if you want no dye transfer on parts, otherwise colored terry ($32).")]}}

P["guide-revendeur"] = {"kind": "guide", "img": SHOP, "rel": ["gros", "garage", "guide-prix"],
 "fr": {"path": "/guides/demarrer-entreprise-revente-chiffons/", "short": "Démarrer une entreprise de revente de chiffons",
  "title": "Idée d'entreprise : revendre des chiffons en camion",
  "desc": "Idée d'affaires au Québec : achetez des guenilles au prix distributeur à Laval, remplissez votre camion et vendez-les aux garages et aux usines.",
  "eyebrow": "Guide · idée d'affaires", "h1": "Idée d'entreprise : revendre des chiffons recyclés aux garages et aux usines",
  "lede": "Une petite entreprise simple à démarrer : achetez vos sacs au prix distributeur chez Entretien Laval, chargez votre camion ou votre fourgonnette et vendez-les comptant à vos clients.",
  "card": "Prix distributeur, camion, clients : comment démarrer.", "alt": "Sacs de chiffons d'atelier prêts à revendre",
  "body": """<h2>Pourquoi les chiffons</h2>
<p>Les garages, ateliers d'usinage et de soudure, usines, fermes et entreprises d'entretien utilisent des chiffons chaque semaine. C'est un produit qui se consomme et se rachète : un client satisfait recommande régulièrement. Dans beaucoup de régions, surtout au nord de Montréal (Laurentides, Lanaudière, Mauricie, Abitibi, Saguenay–Lac-Saint-Jean), peu de fournisseurs passent directement chez les petites entreprises.</p>
<h2>Votre prix d'achat</h2>
<p>Dès 50 sacs de 25 lb, vous payez le prix distributeur (avant taxes) :</p>
<ul><li>T-shirt ou ratine de couleur : 28 $ le [pack] au lieu de 32 $</li>
<li>T-shirt ou ratine blanc : 38 $ le [pack] au lieu de 42 $</li></ul>
<p>Prix spécial revendeur : ramassage seulement, sans livraison. Vous venez chercher vos sacs au 1355 boul. Le Corbusier, à Laval, et vous pouvez mélanger les produits.</p>
<h2>Comment ça fonctionne</h2>
<ol><li>Écrivez à info@entretienlaval.ca avec les produits et le nombre de sacs (minimum 50).</li>
<li>Payez la commande et convenez de l'heure de chargement.</li>
<li>Chargez votre camion ou votre fourgonnette à Laval.</li>
<li>Faites votre tournée : garages, concessionnaires, ateliers, usines, fermes, entreprises de ménage. Vous fixez votre prix de revente et vous encaissez directement.</li>
<li>Revenez remplir le camion quand votre stock baisse.</li></ol>
<h2>Exemple de calcul</h2>
<p>Exemple seulement : 50 sacs de couleur coûtent 1 400 $ avant taxes. Si vous les revendez 40 $ le sac, vous encaissez 2 000 $, soit 600 $ de marge brute avant votre essence, votre temps et vos taxes. Le prix de revente, vos clients et votre région dépendent de vous; Entretien Laval ne garantit pas de revenu.</p>
<h2>Conseils pour bien démarrer</h2>
<ul><li>Commencez par les garages et les ateliers de votre région : ce sont les plus gros utilisateurs.</li>
<li>Gardez des sacs blancs pour les peintres, les ébénistes et les ateliers de finition.</li>
<li>Passez à intervalles réguliers : vos clients prennent l'habitude de racheter.</li>
<li>Informez-vous sur les obligations d'un travailleur autonome ou d'une entreprise au Québec (inscription au Registraire des entreprises, taxes) auprès des services gouvernementaux.</li></ul>""",
  "faq": [("Quelle petite entreprise démarrer avec un camion au Québec?", "La revente de chiffons d'essuyage recyclés aux garages, ateliers et usines est une option simple : Entretien Laval, à Laval, vend aux revendeurs au prix distributeur dès 50 sacs de 25 lb (28 $ couleur, 38 $ blanc, avant taxes), en ramassage seulement au 1355 boul. Le Corbusier. Vous chargez votre camion à Laval et fixez votre prix de revente."),
          ("Faut-il un local ou un entrepôt pour revendre des chiffons?", "Non, pas pour commencer. Vous pouvez acheter 50 sacs, les transporter dans votre camion et revenir à Laval quand votre stock baisse."),
          ("Entretien Laval garantit-il un revenu aux revendeurs?", "Non. Nous fournissons les chiffons au prix distributeur; votre prix de revente, vos clients et vos résultats dépendent de vous.")]},
 "en": {"path": "/en/guides/start-rag-resale-business/", "short": "Start a rag resale business",
  "title": "Business idea: sell shop rags from your truck",
  "desc": "Small business idea in Québec: buy recycled rags at distributor price in Laval, fill your truck or van and sell them to garages and factories.",
  "eyebrow": "Guide · business idea", "h1": "Business idea: resell recycled rags to garages and factories",
  "lede": "A simple small business to start: buy your bags at distributor price from Entretien Laval, load your truck or van and sell them for cash to your customers.",
  "card": "Distributor price, truck, customers: how to start.", "alt": "Bags of shop rags ready to resell",
  "body": """<h2>Why rags</h2>
<p>Garages, machine and welding shops, factories, farms and cleaning companies use rags every week. It's a consumable that gets bought again and again: a happy customer reorders regularly. In many regions, especially north of Montréal (Laurentides, Lanaudière, Mauricie, Abitibi, Saguenay–Lac-Saint-Jean), few suppliers visit small businesses in person.</p>
<h2>Your buying price</h2>
<p>From 50 bags of 25 lb, you pay the distributor price (before tax):</p>
<ul><li>Colored T-shirt or terry: $28 per [pack] instead of $32</li>
<li>White T-shirt or terry: $38 per [pack] instead of $42</li></ul>
<p>Special reseller price: pickup only, no delivery. You collect your bags at 1355 boul. Le Corbusier, Laval, and mixed products are fine.</p>
<h2>How it works</h2>
<ol><li>Email info@entretienlaval.ca with the products and number of bags (minimum 50).</li>
<li>Pay for the order and agree on a loading time.</li>
<li>Load your truck or van in Laval.</li>
<li>Do your route: garages, dealerships, shops, factories, farms, cleaning companies. You set your resale price and collect payment directly.</li>
<li>Come back to refill when your stock runs low.</li></ol>
<h2>Example</h2>
<p>Example only: 50 colored bags cost $1,400 before tax. If you resell them at $40 a bag, you collect $2,000, a $600 gross margin before fuel, your time and taxes. Your resale price, customers and region are up to you; Entretien Laval does not guarantee any income.</p>
<h2>Tips to get started</h2>
<ul><li>Start with garages and shops in your area: they are the biggest users.</li>
<li>Keep white bags for painters, cabinetmakers and finishing shops.</li>
<li>Visit on a regular schedule: customers get used to reordering.</li>
<li>Check the obligations for self-employed workers or businesses in Québec (business registration, sales taxes) with government services.</li></ul>""",
  "faq": [("What small business can I start with a truck in Québec?", "Reselling recycled wiping rags to garages, shops and factories is a simple option: Entretien Laval, in Laval, sells to resellers at distributor price from 50 bags of 25 lb ($28 colored, $38 white, before tax), pickup only at 1355 boul. Le Corbusier. You load your truck in Laval and set your own resale price."),
          ("Do I need a warehouse to resell rags?", "No, not to start. You can buy 50 bags, carry them in your truck and come back to Laval when your stock runs low."),
          ("Does Entretien Laval guarantee income to resellers?", "No. We supply the rags at distributor price; your resale price, customers and results are up to you.")]}}

GUIDE2_PAGES = P
