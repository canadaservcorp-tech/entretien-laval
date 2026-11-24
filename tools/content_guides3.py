"""Guides, batch 3: questions not covered by the earlier guides.

- how many rags a garage uses per month (method, not a made-up average)
- rags for glass and stainless steel
- rags and solvents (acetone, thinner, mineral spirits, alcohol)
- soiled rags at work: storage, pickup and disposal rules for businesses
- buying rags in bulk for a business (end users, not resellers)
- cleaning up an oil spill with rags
Terry is out of stock: these guides only recommend the T-shirt rags.
"""
BAG, SHOP, WHITE, BAGS, WARE = ("sac-chiffons-t-shirt-couleur-25-lb.webp", "sac-de-chiffons-d-atelier-conditionnes-prets-a-l-u.webp",
    "sacs-chiffons-blancs-25-lb.webp", "sacs-chiffons-couleur-25-lb.webp", "entrepot-sacs-chiffons-blancs-et-couleur.webp")
P = {}

P["guide-garage-mois"] = {"kind": "guide", "img": BAG, "rel": ["calculateur", "guide-prix", "p-tshirt-couleur"],
 "fr": {"path": "/guides/combien-chiffons-par-mois-garage/", "short": "Combien de chiffons par mois pour un garage",
  "title": "Combien de chiffons par mois pour un garage? Méthode simple",
  "desc": "Combien de sacs de chiffons un garage utilise-t-il par mois? Une méthode en 4 étapes pour mesurer votre consommation, des exemples chiffrés et le budget.",
  "eyebrow": "Guide · garages", "h1": "Combien de chiffons par mois pour un garage?",
  "lede": "Chaque garage est différent : le nombre de baies, le type de travaux et les habitudes des mécaniciens changent tout. Voici comment mesurer votre vraie consommation en quelques semaines.",
  "card": "Mesurer sa consommation, exemples chiffrés et budget mensuel.", "alt": "Sac de chiffons t-shirt couleur pour garage",
  "body": """<h2>Pourquoi il n'y a pas de chiffre universel</h2>
<p>Un atelier de mécanique générale, un centre de pneus et une carrosserie n'essuient pas la même chose. Un garage qui fait beaucoup de vidanges d'huile et de freins utilise plus de chiffons qu'un garage spécialisé en électronique. Plutôt qu'une moyenne inventée, mesurez votre propre consommation.</p>
<h2>La méthode en 4 étapes</h2>
<ol><li><b>Commandez une quantité de départ</b> : 2 à 4 [packs] de <a href="{{p-tshirt-couleur}}">t-shirt couleur</a> suffisent pour commencer.</li>
<li><b>Notez la date d'ouverture</b> de chaque sac au marqueur, directement sur le sac.</li>
<li><b>Notez la date où il est vide.</b> Après deux ou trois sacs, vous avez une moyenne fiable.</li>
<li><b>Calculez</b> : livres par semaine = 25 lb × nombre de sacs utilisés ÷ nombre de semaines. Entrez ce chiffre dans le <a href="{{calculateur}}">calculateur</a> pour obtenir vos sacs par mois et votre budget avec taxes.</li></ol>
<h2>Exemples chiffrés</h2>
<p>Le calcul se fait avec un mois de 52 ÷ 12 semaines, arrondi au sac supérieur, au prix du t-shirt couleur (32 $ le [pack], avant taxes) :</p>
<table><thead><tr><th>Si vous utilisez…</th><th>Sacs par mois</th><th>Ramassage à Laval</th><th>Livré à Laval (15 $)</th></tr></thead><tbody>
<tr><td>1 sac toutes les 2 semaines (12,5 lb/sem.)</td><td>3</td><td>96 $</td><td>111 $</td></tr>
<tr><td>1 sac par semaine (25 lb/sem.)</td><td>5</td><td>160 $</td><td>175 $</td></tr>
<tr><td>2 sacs par semaine (50 lb/sem.)</td><td>9</td><td>288 $</td><td>303 $</td></tr></tbody></table>
<p>Ce sont des exemples de calcul, pas des moyennes de l'industrie. La livraison coûte 15 $ par commande à Laval (dès 1 sac), 25 $ à Montréal et 35 $ sur la Rive-Nord et la Rive-Sud (dès 2 sacs). Ailleurs, <a href="{{home#devis}}">contactez-nous</a>.</p>
<h2>Réduire la consommation sans perdre de temps</h2>
<ul><li><b>Un bac par baie</b> : les chiffons restent à portée de main et ne traînent pas sur les établis.</li>
<li><b>Le bon chiffon au bon endroit</b> : couleur pour la mécanique, <a href="{{p-tshirt-blanc}}">blanc</a> seulement pour la carrosserie et les surfaces peintes.</li>
<li><b>Un contenant métallique fermé</b> pour les chiffons huileux, vidé chaque jour. Voir <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</li>
<li><b>Les chiffons peu sales</b> (eau, poussière) peuvent être lavés et réutilisés. Voir <a href="{{guide-ranger}}">ranger, laver et jeter ses chiffons</a>.</li></ul>
<h2>Commander au bon rythme</h2>
<p>Une fois votre consommation connue, vous pouvez demander une livraison automatique toutes les 2 semaines ou chaque mois, au même prix. Voir aussi les <a href="{{garage}}">chiffons de garage</a>.</p>""",
  "faq": [("Combien de chiffons y a-t-il dans un sac de 25 lb?", "Nous vendons au poids, car la taille des morceaux varie. C'est pourquoi la méthode se base sur les livres utilisées par semaine plutôt que sur un nombre de chiffons."),
          ("Quel chiffon commander pour un garage?", "Le t-shirt couleur à 32 $ le [pack] pour la mécanique. Gardez du t-shirt blanc à 42 $ pour la carrosserie. La ratine est en rupture de stock pour le moment."),
          ("Peut-on être livré chaque mois sans rappeler?", "Oui. Choisissez la quantité et le rythme (toutes les 2 semaines ou chaque mois) : nous livrons au même prix, avec facture.")]},
 "en": {"path": "/en/guides/how-many-rags-per-month-garage/", "short": "How many rags a garage uses per month",
  "title": "How many shop rags does a garage use per month?",
  "desc": "How many bags of rags does a garage go through each month? A 4-step method to measure your real usage, worked examples and the monthly budget.",
  "eyebrow": "Guide · garages", "h1": "How many shop rags does a garage use per month?",
  "lede": "Every garage is different: the number of bays, the type of work and each mechanic's habits change everything. Here's how to measure your real usage in a few weeks.",
  "card": "Measure your usage, worked examples and monthly budget.", "alt": "Bag of coloured T-shirt rags for a garage",
  "body": """<h2>Why there's no universal number</h2>
<p>A general repair shop, a tire centre and a body shop don't wipe the same things. A garage doing lots of oil changes and brake jobs uses more rags than one focused on electronics. Instead of a made-up average, measure your own usage.</p>
<h2>The 4-step method</h2>
<ol><li><b>Order a starting quantity</b>: 2 to 4 [packs] of <a href="{{p-tshirt-couleur}}">coloured T-shirt</a> rags are enough to start.</li>
<li><b>Write the opening date</b> on each bag with a marker.</li>
<li><b>Write the date it's empty.</b> After two or three bags, you have a reliable average.</li>
<li><b>Calculate</b>: pounds per week = 25 lb × bags used ÷ number of weeks. Enter that number in the <a href="{{calculateur}}">calculator</a> to get your bags per month and budget with tax.</li></ol>
<h2>Worked examples</h2>
<p>Calculated with a month of 52 ÷ 12 weeks, rounded up to the next bag, at the coloured T-shirt price ($32 per [pack], before tax):</p>
<table><thead><tr><th>If you use…</th><th>Bags per month</th><th>Pickup in Laval</th><th>Delivered in Laval ($15)</th></tr></thead><tbody>
<tr><td>1 bag every 2 weeks (12.5 lb/week)</td><td>3</td><td>$96</td><td>$111</td></tr>
<tr><td>1 bag a week (25 lb/week)</td><td>5</td><td>$160</td><td>$175</td></tr>
<tr><td>2 bags a week (50 lb/week)</td><td>9</td><td>$288</td><td>$303</td></tr></tbody></table>
<p>These are example calculations, not industry averages. Delivery is $15 per order in Laval (from 1 bag), $25 in Montréal and $35 on the North and South Shores (from 2 bags). Elsewhere, <a href="{{home#devis}}">contact us</a>.</p>
<h2>Using fewer rags without losing time</h2>
<ul><li><b>One bin per bay</b>: rags stay within reach and don't pile up on benches.</li>
<li><b>The right rag in the right place</b>: coloured for mechanics, <a href="{{p-tshirt-blanc}}">white</a> only for body work and painted surfaces.</li>
<li><b>A closed metal container</b> for oily rags, emptied daily. See <a href="{{guide-huileux}}">oily rags and fire risk</a>.</li>
<li><b>Lightly soiled rags</b> (water, dust) can be washed and reused. See <a href="{{guide-ranger}}">storing, washing and disposing of rags</a>.</li></ul>
<h2>Ordering at the right pace</h2>
<p>Once you know your usage, you can ask for automatic delivery every 2 weeks or every month, at the same price. See also <a href="{{garage}}">garage shop rags</a>.</p>""",
  "faq": [("How many rags are in a 25 lb bag?", "We sell by weight because piece sizes vary. That's why the method uses pounds per week rather than a number of rags."),
          ("Which rag should a garage order?", "Coloured T-shirt rags at $32 per [pack] for mechanics. Keep white T-shirt rags at $42 for body work. Terry is out of stock for now."),
          ("Can I get monthly delivery without calling?", "Yes. Choose the quantity and schedule (every 2 weeks or every month): we deliver at the same price, with an invoice.")]}}

P["guide-vitres"] = {"kind": "guide", "img": WHITE, "rel": ["p-tshirt-blanc", "entretien", "esthetique-auto"],
 "fr": {"path": "/guides/chiffon-vitres-inox/", "short": "Chiffons pour vitres et inox",
  "title": "Quel chiffon pour les vitres et l'inox sans traces?",
  "desc": "Le bon chiffon pour nettoyer les vitres, les miroirs et l'inox sans traces : coton blanc peu pelucheux, technique dans le sens du grain et erreurs à éviter.",
  "eyebrow": "Guide · entretien", "h1": "Quel chiffon pour les vitres et l'inox?",
  "lede": "Pour les vitres, les miroirs et l'acier inoxydable, il faut un chiffon propre, sec et peu pelucheux. Parmi nos produits, c'est le t-shirt blanc.",
  "card": "Vitres, miroirs, inox : le bon chiffon et la bonne technique.", "alt": "Sacs de chiffons blancs recyclés",
  "body": """<h2>Le bon chiffon : t-shirt de coton blanc</h2>
<p>Le <a href="{{p-tshirt-blanc}}">t-shirt blanc</a> est un jersey de coton mince : il absorbe l'eau, laisse peu de peluches et ne dépose aucune teinture. C'est notre meilleur choix pour les vitres et l'inox. Le coton recyclé n'est pas totalement sans peluches : voir <a href="{{guide-peluches}}">chiffon non pelucheux</a>.</p>
<h2>Vitres et miroirs</h2>
<ol><li>Enlevez d'abord la poussière et la grosse saleté avec un chiffon humide.</li>
<li>Appliquez votre nettoyant à vitres habituel, sans détremper.</li>
<li>Essuyez avec un chiffon blanc propre, puis <b>finissez avec un deuxième chiffon sec</b> : c'est l'étape qui enlève les traces.</li>
<li>Changez de chiffon dès qu'il est humide : un chiffon mouillé étale la saleté.</li></ol>
<p>Pour les grandes vitrines, la raclette fait le gros du travail; le chiffon sec sert aux bords et aux coins.</p>
<h2>Acier inoxydable</h2>
<ul><li><b>Essuyez dans le sens du grain</b> (les fines lignes du métal brossé), jamais en cercles.</li>
<li>Utilisez de l'eau savonneuse ou un nettoyant pour inox, puis séchez avec un chiffon blanc sec.</li>
<li><b>Évitez l'eau de Javel et les produits chlorés</b> sur l'inox, ainsi que les tampons abrasifs : ils peuvent marquer la surface.</li>
<li>Suivez toujours les consignes du fabricant de l'équipement et du produit nettoyant.</li></ul>
<h2>Erreurs fréquentes</h2>
<ul><li><b>Assouplissant</b> : si vous lavez vos chiffons, n'en mettez pas. Il laisse un film qui fait des traces et réduit l'absorption.</li>
<li><b>Chiffon couleur</b> : avec certains nettoyants, un tissu teint peut déteindre sur les joints ou les surfaces pâles.</li>
<li><b>Même chiffon pour tout</b> : gardez des chiffons blancs réservés aux vitres, séparés de ceux de la cuisine ou de l'atelier.</li></ul>
<h2>Où on l'utilise</h2>
<p>Halls d'immeubles, vitrines, cuisines commerciales, ascenseurs, salles de bain, ateliers d'esthétique automobile. Voir <a href="{{entretien}}">entretien ménager et conciergerie</a> et <a href="{{restauration}}">restaurants et cuisines</a>.</p>""",
  "faq": [("Quel chiffon pour laver les vitres sans traces?", "Un chiffon de coton blanc mince, propre et sec pour la finition. Parmi nos produits : le t-shirt blanc, 42 $ le [pack] de 25 lb avant taxes."),
          ("Faut-il essuyer l'inox en cercles?", "Non. Essuyez dans le sens du grain du métal pour éviter les marques, puis séchez avec un chiffon sec."),
          ("Le coton recyclé remplace-t-il la microfibre pour les vitres?", "Pour la plupart des vitres et de l'inox, un t-shirt blanc propre fait bien le travail. La microfibre reste utile pour les surfaces très délicates ou les écrans.")]},
 "en": {"path": "/en/guides/rags-for-glass-stainless-steel/", "short": "Rags for glass and stainless steel",
  "title": "Best rag for glass and stainless steel without streaks",
  "desc": "The right rag for streak-free windows, mirrors and stainless steel: low-lint white cotton, wiping with the grain, and the mistakes to avoid.",
  "eyebrow": "Guide · cleaning", "h1": "Which rag for glass and stainless steel?",
  "lede": "For windows, mirrors and stainless steel you need a clean, dry, low-lint rag. Among our products, that's the white T-shirt rag.",
  "card": "Glass, mirrors, stainless steel: the right rag and technique.", "alt": "Bags of white recycled rags",
  "body": """<h2>The right rag: white cotton T-shirt</h2>
<p><a href="{{p-tshirt-blanc}}">White T-shirt rags</a> are thin cotton jersey: they absorb water, leave little lint and transfer no dye. They're our best pick for glass and stainless steel. Recycled cotton isn't completely lint-free: see <a href="{{guide-peluches}}">lint-free rags</a>.</p>
<h2>Windows and mirrors</h2>
<ol><li>First remove dust and heavy dirt with a damp rag.</li>
<li>Apply your usual glass cleaner, without soaking the surface.</li>
<li>Wipe with a clean white rag, then <b>finish with a second, dry rag</b>: that's the step that removes streaks.</li>
<li>Switch rags as soon as one gets damp: a wet rag just spreads dirt.</li></ol>
<p>For large shop windows, a squeegee does most of the work; the dry rag handles edges and corners.</p>
<h2>Stainless steel</h2>
<ul><li><b>Wipe with the grain</b> (the fine lines in brushed metal), never in circles.</li>
<li>Use soapy water or a stainless steel cleaner, then dry with a dry white rag.</li>
<li><b>Avoid bleach and chlorine products</b> on stainless steel, as well as abrasive pads: they can mark the surface.</li>
<li>Always follow the equipment and cleaner manufacturers' directions.</li></ul>
<h2>Common mistakes</h2>
<ul><li><b>Fabric softener</b>: if you wash your rags, skip it. It leaves a film that streaks and reduces absorbency.</li>
<li><b>Coloured rags</b>: with some cleaners, dyed fabric can bleed onto grout or pale surfaces.</li>
<li><b>One rag for everything</b>: keep white rags just for glass, separate from kitchen or shop rags.</li></ul>
<h2>Where it's used</h2>
<p>Building lobbies, shop windows, commercial kitchens, elevators, washrooms, car detailing shops. See <a href="{{entretien}}">janitorial and building maintenance</a> and <a href="{{restauration}}">restaurants and kitchens</a>.</p>""",
  "faq": [("Which rag cleans windows without streaks?", "A thin white cotton rag, clean, with a dry one for the final wipe. Among our products: white T-shirt rags, $42 per 25 lb [pack] before tax."),
          ("Should stainless steel be wiped in circles?", "No. Wipe with the grain of the metal to avoid marks, then dry with a dry rag."),
          ("Does recycled cotton replace microfiber for glass?", "For most glass and stainless steel, a clean white T-shirt rag does the job well. Microfiber is still useful for very delicate surfaces or screens.")]}}

P["guide-solvants"] = {"kind": "guide", "img": SHOP, "rel": ["p-tshirt-blanc", "industrie", "guide-huileux"],
 "fr": {"path": "/guides/chiffons-solvants-acetone-diluant/", "short": "Chiffons et solvants : acétone, diluant, varsol",
  "title": "Chiffon pour solvants : acétone, diluant, varsol, alcool",
  "desc": "Quel chiffon utiliser avec l'acétone, le diluant à peinture, le varsol ou l'alcool isopropylique? Coton, blanc ou couleur, sécurité et rangement après usage.",
  "eyebrow": "Guide · solvants", "h1": "Quel chiffon utiliser avec les solvants?",
  "lede": "Acétone, diluant à laque, varsol, alcool isopropylique : le coton supporte la plupart des solvants d'atelier. Le choix important, c'est la couleur, et ce que vous faites du chiffon après.",
  "card": "Acétone, diluant, varsol, alcool : quel chiffon et quelles précautions.", "alt": "Sac de chiffons d'atelier pour solvants",
  "body": """<h2>Pourquoi le coton</h2>
<p>Le coton est une fibre naturelle qui supporte la plupart des solvants d'atelier courants : il absorbe sans fondre. Certains tissus synthétiques, au contraire, peuvent ramollir ou se dissoudre au contact de solvants forts comme l'acétone. Nos chiffons sont faits de vêtements de coton recyclé; comme un t-shirt récupéré peut contenir un peu de fibres mélangées, faites un essai sur un morceau avant un usage critique.</p>
<h2>Blanc ou couleur?</h2>
<p>Avec un solvant, un tissu teint peut <b>déteindre</b> sur la surface. Pour nettoyer une pièce, préparer une surface avant la peinture ou la colle, ou essuyer une presse d'imprimerie, prenez le <a href="{{p-tshirt-blanc}}">t-shirt blanc</a>. Pour nettoyer des outils ou essuyer les mains, le <a href="{{p-tshirt-couleur}}">t-shirt couleur</a> coûte moins cher.</p>
<table><thead><tr><th>Solvant</th><th>Usage courant</th><th>Chiffon conseillé</th></tr></thead><tbody>
<tr><td>Acétone</td><td>Dégraissage, résine, colle</td><td>T-shirt blanc</td></tr>
<tr><td>Diluant à laque ou à peinture</td><td>Nettoyage de pistolets et d'outils</td><td>Couleur pour les outils, blanc pour les surfaces</td></tr>
<tr><td>Varsol (essence minérale)</td><td>Pinceaux, dégraissage</td><td>Couleur ou blanc</td></tr>
<tr><td>Alcool isopropylique</td><td>Préparation de surface avant collage ou peinture</td><td>T-shirt blanc</td></tr></tbody></table>
<p>Ces solvants ne remplacent pas les consignes du fabricant : lisez toujours la fiche de données de sécurité (FDS) du produit, prévue par le SIMDUT.</p>
<h2>Quand ne pas utiliser de chiffon de coton</h2>
<ul><li><b>Acides et bases forts</b> : le coton peut être attaqué. Utilisez le matériel d'absorption indiqué dans la FDS.</li>
<li><b>Électronique, salles blanches, optique</b> : il faut des lingettes spécialisées non tissées, que nous ne vendons pas.</li></ul>
<h2>Sécurité pendant l'usage</h2>
<ul><li>Travaillez dans un endroit ventilé, loin des flammes et des étincelles : les vapeurs de solvant s'enflamment facilement.</li>
<li>Portez les gants indiqués dans la FDS.</li>
<li>Ne mettez que la quantité nécessaire sur le chiffon, jamais directement dans un bac ouvert de chiffons.</li></ul>
<h2>Après usage</h2>
<p>Un chiffon imbibé de solvant va dans un <b>contenant métallique fermé</b>, jamais à la poubelle ordinaire ni dans une sécheuse. Pour les règles d'entreposage et d'élimination en entreprise, voir <a href="{{guide-souilles}}">chiffons souillés en entreprise</a>. Pour l'huile de lin et les teintures, qui peuvent s'enflammer seules, voir <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p>""",
  "faq": [("Peut-on utiliser un chiffon de coton avec de l'acétone?", "Oui, le coton supporte l'acétone. Prenez du blanc pour éviter que la teinture déteigne, travaillez dans un endroit ventilé et rangez le chiffon usé dans un contenant métallique fermé."),
          ("Pourquoi un chiffon blanc avec les solvants?", "Parce qu'un solvant peut dissoudre la teinture d'un tissu coloré et la déposer sur la surface. Le blanc élimine ce risque."),
          ("Un chiffon imbibé de solvant peut-il aller à la poubelle?", "Non. Gardez-le dans un contenant métallique fermé et éliminez-le selon les règles de votre municipalité ou avec une entreprise de collecte spécialisée.")]},
 "en": {"path": "/en/guides/rags-for-solvents-acetone-thinner/", "short": "Rags and solvents: acetone, thinner, spirits",
  "title": "Best rag for solvents: acetone, thinner, mineral spirits",
  "desc": "Which rag to use with acetone, paint thinner, mineral spirits or isopropyl alcohol? Cotton, white or coloured, safety and storing rags after use.",
  "eyebrow": "Guide · solvents", "h1": "Which rag should you use with solvents?",
  "lede": "Acetone, lacquer thinner, mineral spirits, isopropyl alcohol: cotton handles most shop solvents. What really matters is the colour, and what you do with the rag afterwards.",
  "card": "Acetone, thinner, mineral spirits, alcohol: which rag and what precautions.", "alt": "Bag of shop rags for solvents",
  "body": """<h2>Why cotton</h2>
<p>Cotton is a natural fibre that handles most common shop solvents: it absorbs without melting. Some synthetic fabrics, on the other hand, can soften or dissolve with strong solvents such as acetone. Our rags are made from recycled cotton clothing; since a recovered T-shirt may contain some blended fibres, test a piece before critical work.</p>
<h2>White or coloured?</h2>
<p>With a solvent, dyed fabric can <b>bleed</b> onto the surface. To clean a part, prep a surface before paint or glue, or wipe a printing press, use <a href="{{p-tshirt-blanc}}">white T-shirt rags</a>. To clean tools or wipe hands, <a href="{{p-tshirt-couleur}}">coloured T-shirt rags</a> cost less.</p>
<table><thead><tr><th>Solvent</th><th>Common use</th><th>Recommended rag</th></tr></thead><tbody>
<tr><td>Acetone</td><td>Degreasing, resin, glue</td><td>White T-shirt</td></tr>
<tr><td>Lacquer or paint thinner</td><td>Cleaning spray guns and tools</td><td>Coloured for tools, white for surfaces</td></tr>
<tr><td>Mineral spirits (varsol)</td><td>Brushes, degreasing</td><td>Coloured or white</td></tr>
<tr><td>Isopropyl alcohol</td><td>Surface prep before bonding or painting</td><td>White T-shirt</td></tr></tbody></table>
<p>This doesn't replace the manufacturer's directions: always read the product's safety data sheet (SDS) under WHMIS.</p>
<h2>When not to use a cotton rag</h2>
<ul><li><b>Strong acids and bases</b>: they can attack cotton. Use the absorbent material listed in the SDS.</li>
<li><b>Electronics, cleanrooms, optics</b>: these need specialized nonwoven wipes, which we don't sell.</li></ul>
<h2>Safety while working</h2>
<ul><li>Work in a ventilated area, away from flames and sparks: solvent vapours ignite easily.</li>
<li>Wear the gloves listed in the SDS.</li>
<li>Put only the amount you need on the rag, never straight into an open bin of rags.</li></ul>
<h2>After use</h2>
<p>A solvent-soaked rag goes in a <b>closed metal container</b>, never in the regular trash or a dryer. For storage and disposal rules at work, see <a href="{{guide-souilles}}">soiled rags at work</a>. For linseed oil and stains, which can self-ignite, see <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p>""",
  "faq": [("Can I use a cotton rag with acetone?", "Yes, cotton handles acetone. Use white so no dye bleeds, work in a ventilated area and put the used rag in a closed metal container."),
          ("Why a white rag with solvents?", "Because a solvent can dissolve the dye in a coloured fabric and leave it on the surface. White removes that risk."),
          ("Can a solvent-soaked rag go in the trash?", "No. Keep it in a closed metal container and dispose of it under your municipality's rules or through a specialized waste pickup company.")]}}

P["guide-souilles"] = {"kind": "guide", "img": SHOP, "rel": ["guide-huileux", "guide-ranger", "industrie"],
 "fr": {"path": "/guides/chiffons-souilles-entreprise-entreposage-elimination/", "short": "Chiffons souillés en entreprise : entreposer et éliminer",
  "title": "Chiffons souillés en entreprise : entreposage et élimination",
  "desc": "Entreprises du Québec : entreposer, faire collecter et éliminer les chiffons souillés d'huile, de solvant ou de peinture. Liste de vérification pratique.",
  "eyebrow": "Guide · entreprises", "h1": "Chiffons souillés en entreprise : entreposer, faire collecter, éliminer",
  "lede": "Dans un garage, un atelier ou une usine, les chiffons souillés sont une question de sécurité incendie et d'environnement. Voici une procédure simple à mettre en place, et les points à vérifier avec les autorités.",
  "card": "Contenants, procédure, collecte : la liste de vérification pour les entreprises.", "alt": "Chiffons d'atelier conditionnés",
  "body": """<h2>Trois catégories de chiffons</h2>
<ul><li><b>Propres</b> : dans leur sac fermé ou un bac à couvercle, loin des produits chimiques.</li>
<li><b>Peu sales</b> (eau, poussière, nettoyants doux) : ils peuvent être lavés et réutilisés. Voir <a href="{{guide-ranger}}">ranger, laver et jeter ses chiffons</a>.</li>
<li><b>Souillés</b> (huile, graisse, solvants, carburant, peinture, teinture) : ils suivent la procédure ci-dessous.</li></ul>
<h2>Entreposer les chiffons souillés</h2>
<ol><li><b>Contenant métallique à couvercle à fermeture automatique</b>, prévu pour les chiffons huileux, à chaque poste de travail où l'on utilise des huiles ou des solvants.</li>
<li><b>Identifié clairement</b> (« Chiffons souillés seulement ») pour qu'on n'y jette rien d'autre.</li>
<li><b>Loin des sources de chaleur</b> : soudure, chauffage, compresseur, rayons du soleil.</li>
<li><b>Vidé chaque jour</b> ou à la fin de chaque quart dans un contenant d'entreposage fermé, à l'écart du bâtiment si possible.</li>
<li><b>Jamais en tas</b>, jamais dans une poubelle ouverte ni dans une sécheuse. Les chiffons imbibés d'huile de lin ou de teinture peuvent s'enflammer seuls : voir <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</li></ol>
<h2>Faire collecter et éliminer</h2>
<p>Selon le produit absorbé, des chiffons souillés peuvent être considérés comme des <b>matières dangereuses résiduelles</b> au sens du Règlement sur les matières dangereuses du Québec. Ils ne vont donc pas à la poubelle ordinaire. En pratique, les entreprises :</p>
<ul><li>font appel à une <b>entreprise de collecte de matières dangereuses</b> qui fournit souvent les contenants et assure le transport;</li>
<li>ou utilisent un <b>service de location et de lavage de chiffons industriels</b>, qui reprend les chiffons sales;</li>
<li>conservent les <b>preuves de collecte</b> (bons, factures) pour leurs dossiers.</li></ul>
<p>Les règles exactes dépendent des produits utilisés, des quantités et de votre municipalité. Vérifiez-les auprès du ministère de l'Environnement du Québec, de votre municipalité et de votre collecteur.</p>
<h2>Former l'équipe</h2>
<ul><li>Les produits utilisés sont couverts par le SIMDUT : les fiches de données de sécurité (FDS) indiquent comment entreposer et éliminer les matières souillées.</li>
<li>Affichez la procédure près des contenants et montrez-la à chaque nouvel employé.</li>
<li>En cas de doute sur la prévention des incendies, consultez le service de sécurité incendie de votre municipalité.</li></ul>
<h2>Liste de vérification</h2>
<ul><li>Un contenant métallique à fermeture automatique par zone de travail.</li>
<li>Contenants identifiés, vidés chaque jour.</li>
<li>Chiffons propres séparés des chiffons souillés.</li>
<li>Un collecteur ou un service de lavage choisi, avec preuves de collecte conservées.</li>
<li>FDS accessibles et équipe formée.</li></ul>
<p>Pour vos chiffons neufs : <a href="{{p-tshirt-couleur}}">t-shirt couleur</a> à 32 $ ou <a href="{{p-tshirt-blanc}}">t-shirt blanc</a> à 42 $ le [pack]. Voir aussi les <a href="{{industrie}}">chiffons industriels</a>.</p>""",
  "faq": [("Un chiffon huileux peut-il aller à la poubelle de l'entreprise?", "Non. Gardez-le dans un contenant métallique fermé et faites-le collecter par une entreprise spécialisée ou un service de lavage de chiffons industriels, selon les règles qui s'appliquent à vous."),
          ("Les chiffons souillés sont-ils des matières dangereuses?", "Cela dépend du produit absorbé et des quantités. Selon le cas, ils peuvent être des matières dangereuses résiduelles au sens du Règlement sur les matières dangereuses du Québec. Vérifiez avec votre collecteur ou le ministère de l'Environnement."),
          ("Faut-il un contenant spécial pour les chiffons huileux?", "Un contenant métallique avec un couvercle à fermeture automatique, conçu pour les chiffons huileux, est la pratique recommandée. Videz-le chaque jour.")]},
 "en": {"path": "/en/guides/soiled-rags-business-storage-disposal/", "short": "Soiled rags at work: storage and disposal",
  "title": "Soiled rags at work: storage, pickup and disposal",
  "desc": "Québec businesses: how to store, have collected and dispose of rags soiled with oil, solvent or paint. A practical checklist for shops and plants.",
  "eyebrow": "Guide · businesses", "h1": "Soiled rags at work: storage, pickup and disposal",
  "lede": "In a garage, shop or plant, soiled rags are a fire-safety and environmental issue. Here's a simple procedure to set up, and what to check with the authorities.",
  "card": "Containers, procedure, pickup: the checklist for businesses.", "alt": "Packed shop rags",
  "body": """<h2>Three kinds of rags</h2>
<ul><li><b>Clean</b>: in their closed bag or a lidded bin, away from chemicals.</li>
<li><b>Lightly soiled</b> (water, dust, mild cleaners): can be washed and reused. See <a href="{{guide-ranger}}">storing, washing and disposing of rags</a>.</li>
<li><b>Soiled</b> (oil, grease, solvents, fuel, paint, stain): follow the procedure below.</li></ul>
<h2>Storing soiled rags</h2>
<ol><li><b>A metal container with a self-closing lid</b>, made for oily rags, at every workstation where oils or solvents are used.</li>
<li><b>Clearly labelled</b> (“Soiled rags only”) so nothing else goes in.</li>
<li><b>Away from heat sources</b>: welding, heaters, compressors, direct sunlight.</li>
<li><b>Emptied daily</b> or at the end of each shift into a closed storage container, away from the building if possible.</li>
<li><b>Never in a pile</b>, never in an open trash can or a dryer. Rags soaked with linseed oil or stain can self-ignite: see <a href="{{guide-huileux}}">oily rags and fire risk</a>.</li></ol>
<h2>Pickup and disposal</h2>
<p>Depending on what they absorbed, soiled rags may be considered <b>residual hazardous materials</b> under Québec's Regulation respecting hazardous materials. So they don't go in the regular trash. In practice, businesses:</p>
<ul><li>use a <b>hazardous waste pickup company</b>, which often supplies the containers and handles transport;</li>
<li>or use an <b>industrial shop towel rental and laundry service</b> that takes back the dirty rags;</li>
<li>keep <b>proof of pickup</b> (slips, invoices) on file.</li></ul>
<p>The exact rules depend on the products used, the quantities and your municipality. Check them with Québec's Ministry of the Environment, your municipality and your waste hauler.</p>
<h2>Training the team</h2>
<ul><li>The products you use fall under WHMIS: their safety data sheets (SDS) explain how to store and dispose of soiled materials.</li>
<li>Post the procedure near the containers and show it to every new employee.</li>
<li>If in doubt about fire prevention, check with your municipality's fire department.</li></ul>
<h2>Checklist</h2>
<ul><li>One self-closing metal container per work area.</li>
<li>Containers labelled and emptied daily.</li>
<li>Clean rags kept apart from soiled rags.</li>
<li>A waste hauler or laundry service chosen, with proof of pickup kept.</li>
<li>SDSs available and the team trained.</li></ul>
<p>For new rags: <a href="{{p-tshirt-couleur}}">coloured T-shirt</a> at $32 or <a href="{{p-tshirt-blanc}}">white T-shirt</a> at $42 per [pack]. See also <a href="{{industrie}}">industrial rags</a>.</p>""",
  "faq": [("Can an oily rag go in the company trash?", "No. Keep it in a closed metal container and have it collected by a specialized company or an industrial rag laundry service, under the rules that apply to you."),
          ("Are soiled rags hazardous waste?", "It depends on what they absorbed and the quantities. Sometimes they are residual hazardous materials under Québec's Regulation respecting hazardous materials. Check with your waste hauler or the Ministry of the Environment."),
          ("Do oily rags need a special container?", "A metal container with a self-closing lid, designed for oily rags, is the recommended practice. Empty it every day.")]}}

P["guide-entreprise"] = {"kind": "guide", "img": WARE, "rel": ["gros", "calculateur", "commander"],
 "fr": {"path": "/guides/acheter-guenilles-en-gros-entreprise/", "short": "Acheter des guenilles en gros pour une entreprise",
  "title": "Acheter des guenilles en gros pour une entreprise : guide",
  "desc": "Garage, atelier, entreprise d'entretien : comment acheter vos guenilles en gros, choisir le produit, la quantité, la livraison, la facture et le prix de volume.",
  "eyebrow": "Guide · achats", "h1": "Acheter des guenilles en gros pour votre entreprise",
  "lede": "Vous achetez des chiffons pour votre propre entreprise, pas pour les revendre? Voici comment choisir, combien commander, comment se faire livrer et ce qu'il faut pour votre comptabilité.",
  "card": "Produit, quantité, livraison, facture : acheter en volume pour son entreprise.", "alt": "Entrepôt de sacs de chiffons blancs et couleur",
  "body": """<h2>1. Choisir le produit</h2>
<ul><li><a href="{{p-tshirt-couleur}}">T-shirt couleur</a>, 32 $ le [pack] : huile, graisse, outils, mains, ménage courant. Le choix de la plupart des entreprises.</li>
<li><a href="{{p-tshirt-blanc}}">T-shirt blanc</a>, 42 $ le [pack] : peinture, teinture, solvants, vitres, inox, surfaces pâles.</li>
<li>La ratine (couleur et blanche) est en rupture de stock pour le moment.</li></ul>
<p>Tous les chiffons sont en coton recyclé, lavés à l'eau chaude, triés et traités à la chaleur, sans boutons ni fermetures éclair, en [packs] (11,3 kg). Échantillons sur demande.</p>
<h2>2. Estimer la quantité</h2>
<p>Commencez avec quelques sacs, notez combien de temps ils durent, puis utilisez le <a href="{{calculateur}}">calculateur</a>. Pour un garage, voir <a href="{{guide-garage-mois}}">combien de chiffons par mois</a>. Prévoyez de la place : un sac de 25 lb est compact, mais 20 sacs occupent un coin d'entrepôt.</p>
<h2>3. Choisir la livraison ou le ramassage</h2>
<table><thead><tr><th>Zone</th><th>Frais par commande</th><th>Minimum</th></tr></thead><tbody>
<tr><td>Laval</td><td>15 $</td><td>1 sac</td></tr>
<tr><td>Montréal</td><td>25 $</td><td>2 sacs</td></tr>
<tr><td>Rive-Nord et Rive-Sud</td><td>35 $</td><td>2 sacs</td></tr>
<tr><td>Ramassage au 1355 boul. Le Corbusier, Laval</td><td>Gratuit</td><td>1 sac</td></tr></tbody></table>
<p>Livraison en 1 à 3 jours ouvrables après le paiement. Hors de ces zones, <a href="{{home#devis}}">contactez-nous</a> : nous vous dirons ce qui est possible pour votre adresse. Voir les villes desservies dans la page <a href="{{livraison}}">livraison</a>.</p>
<h2>4. Commander et payer</h2>
<ul><li><b>Jusqu'à 10 sacs</b> : <a href="{{commander}}">commande en ligne</a>, paiement par PayPal ou carte de crédit ou de débit.</li>
<li><b>Plus de 10 sacs, ou virement Interac</b> : demandez une <a href="{{home#devis}}">soumission</a> ou écrivez à info@entretienlaval.ca.</li>
<li><b>Livraison régulière</b> : toutes les 2 semaines ou chaque mois, au même prix, sans avoir à rappeler.</li></ul>
<h2>5. Pour la comptabilité</h2>
<p>Vous recevez une facture d'entreprise enregistrée avec TPS et TVQ (Entretien Laval, NEQ 2280629637). Pour vos dossiers d'achat responsable, une fiche fournisseur est offerte dans la page <a href="{{gros}}">guenilles en gros</a>.</p>
<h2>6. Le prix de volume</h2>
<p>Dès 50 sacs, le prix distributeur s'applique : 28 $ en couleur et 38 $ en blanc le [pack], avant taxes, en <b>ramassage seulement</b> à Laval. Une palette compte 45 sacs. Si vous revendez les chiffons, voir <a href="{{guide-revendeur}}">démarrer une entreprise de revente</a>.</p>""",
  "faq": [("Quel est le prix des guenilles en gros pour une entreprise?", "32 $ le [pack] en t-shirt couleur et 42 $ en t-shirt blanc, avant taxes. Dès 50 sacs : 28 $ et 38 $, en ramassage seulement à Laval."),
          ("Livrez-vous les entreprises hors du Grand Montréal?", "La livraison en ligne couvre Laval, Montréal, la Rive-Nord et la Rive-Sud. Ailleurs, contactez-nous au 438-831-3611 ou à info@entretienlaval.ca pour savoir ce qui est possible."),
          ("Puis-je avoir un échantillon avant une grosse commande?", "Oui, sur demande, pour vérifier la qualité et la taille des morceaux.")]},
 "en": {"path": "/en/guides/buying-rags-in-bulk-for-business/", "short": "Buying rags in bulk for a business",
  "title": "Buying rags in bulk for your business: a guide",
  "desc": "Garage, shop, cleaning company: how to buy rags in bulk, choose the product and quantity, delivery, invoicing and the volume price.",
  "eyebrow": "Guide · purchasing", "h1": "Buying rags in bulk for your business",
  "lede": "Buying rags for your own business, not to resell? Here's how to choose, how much to order, how delivery works and what you need for your books.",
  "card": "Product, quantity, delivery, invoice: buying in volume for your business.", "alt": "Warehouse of white and coloured rag bags",
  "body": """<h2>1. Choose the product</h2>
<ul><li><a href="{{p-tshirt-couleur}}">Coloured T-shirt</a>, $32 per [pack]: oil, grease, tools, hands, everyday cleaning. Most businesses' pick.</li>
<li><a href="{{p-tshirt-blanc}}">White T-shirt</a>, $42 per [pack]: paint, stain, solvents, glass, stainless steel, pale surfaces.</li>
<li>Terry (coloured and white) is out of stock for now.</li></ul>
<p>All rags are recycled cotton, washed in hot water, sorted and heat-treated, with no buttons or zippers, in [packs] (11.3 kg). Samples on request.</p>
<h2>2. Estimate the quantity</h2>
<p>Start with a few bags, note how long they last, then use the <a href="{{calculateur}}">calculator</a>. For a garage, see <a href="{{guide-garage-mois}}">how many rags per month</a>. Plan the space: a 25 lb bag is compact, but 20 bags fill a corner of a warehouse.</p>
<h2>3. Choose delivery or pickup</h2>
<table><thead><tr><th>Zone</th><th>Fee per order</th><th>Minimum</th></tr></thead><tbody>
<tr><td>Laval</td><td>$15</td><td>1 bag</td></tr>
<tr><td>Montréal</td><td>$25</td><td>2 bags</td></tr>
<tr><td>North Shore and South Shore</td><td>$35</td><td>2 bags</td></tr>
<tr><td>Pickup at 1355 boul. Le Corbusier, Laval</td><td>Free</td><td>1 bag</td></tr></tbody></table>
<p>Delivered within 1 to 3 business days of payment. Outside these zones, <a href="{{home#devis}}">contact us</a>: we'll tell you what's possible for your address. See the towns we serve on the <a href="{{livraison}}">delivery</a> page.</p>
<h2>4. Order and pay</h2>
<ul><li><b>Up to 10 bags</b>: <a href="{{commander}}">order online</a>, pay with PayPal or a credit or debit card.</li>
<li><b>More than 10 bags, or Interac e-Transfer</b>: request a <a href="{{home#devis}}">quote</a> or email info@entretienlaval.ca.</li>
<li><b>Regular delivery</b>: every 2 weeks or every month, at the same price, without calling again.</li></ul>
<h2>5. For your books</h2>
<p>You get a registered business invoice with GST and QST (Entretien Laval, NEQ 2280629637). For responsible purchasing files, a supplier sheet is available on the <a href="{{gros}}">wholesale rags</a> page.</p>
<h2>6. The volume price</h2>
<p>From 50 bags, the distributor price applies: $28 coloured and $38 white per [pack], before tax, <b>pickup only</b> in Laval. A pallet holds 45 bags. If you resell the rags, see <a href="{{guide-revendeur}}">start a rag resale business</a>.</p>""",
  "faq": [("What do bulk rags cost for a business?", "$32 per [pack] for coloured T-shirt and $42 for white T-shirt, before tax. From 50 bags: $28 and $38, pickup only in Laval."),
          ("Do you deliver to businesses outside Greater Montreal?", "Online delivery covers Laval, Montréal, the North Shore and the South Shore. Elsewhere, contact us at 438-831-3611 or info@entretienlaval.ca to find out what's possible."),
          ("Can I get a sample before a large order?", "Yes, on request, to check the quality and piece size.")]}}

P["guide-deversement"] = {"kind": "guide", "img": BAGS, "rel": ["p-tshirt-couleur", "guide-souilles", "guide-huileux"],
 "fr": {"path": "/guides/nettoyer-deversement-huile-chiffons/", "short": "Nettoyer un déversement d'huile",
  "title": "Nettoyer un déversement d'huile au garage avec des chiffons",
  "desc": "Nettoyer un déversement d'huile ou de carburant sur un plancher de garage ou d'atelier avec des chiffons, étape par étape, et quoi faire des chiffons après.",
  "eyebrow": "Guide · garages et ateliers", "h1": "Nettoyer un déversement d'huile avec des chiffons",
  "lede": "Une vidange qui déborde, un bidon renversé, une fuite sous un véhicule : voici comment ramasser un petit déversement d'huile proprement et en sécurité.",
  "card": "Contenir, absorber, nettoyer, jeter : les étapes pour un petit déversement.", "alt": "Sacs de chiffons couleur",
  "body": """<h2>Avant de commencer</h2>
<ul><li><b>Coupez la source</b> : redressez le bidon, placez un bac sous la fuite.</li>
<li><b>Éloignez les sources d'ignition</b> si c'est de l'essence ou un solvant : pas de flamme, pas d'étincelle, aérez.</li>
<li><b>Portez des gants</b> résistants aux huiles et consultez la fiche de données de sécurité (FDS) du produit.</li></ul>
<h2>Les étapes</h2>
<ol><li><b>Contenez</b> : entourez le déversement de chiffons ou d'un boudin absorbant pour l'empêcher de s'étendre, surtout vers un drain.</li>
<li><b>Absorbez de l'extérieur vers le centre</b> avec des chiffons de <a href="{{p-tshirt-couleur}}">t-shirt couleur</a>. Posez-les, laissez-les boire, ramassez-les sans frotter au début.</li>
<li><b>Mettez chaque chiffon imbibé directement</b> dans un contenant métallique fermé.</li>
<li><b>Dégraissez</b> la tache restante avec un dégraissant pour plancher, puis essuyez avec des chiffons propres.</li>
<li><b>Séchez</b> la surface pour éviter les chutes.</li></ol>
<h2>À ne pas faire</h2>
<ul><li><b>Ne rincez jamais l'huile vers un drain de plancher, un égout pluvial ou un fossé.</b></li>
<li>Ne laissez pas les chiffons imbibés en tas ou dans une poubelle ouverte : voir <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</li>
<li>Ne mettez pas les chiffons huileux dans une laveuse ou une sécheuse.</li></ul>
<h2>Après le nettoyage</h2>
<p>Les chiffons imbibés d'huile, de carburant ou de liquide de refroidissement ne vont pas à la poubelle ordinaire. Les particuliers les apportent à l'écocentre; les entreprises les font collecter par une entreprise spécialisée. Voir <a href="{{guide-souilles}}">chiffons souillés en entreprise</a>.</p>
<h2>Gros déversements</h2>
<p>Les chiffons conviennent aux petits déversements à l'intérieur. Pour un gros volume, une fuite qui atteint le sol, un cours d'eau ou un égout, utilisez une trousse d'intervention prévue à cet effet et signalez-le à Urgence-Environnement du ministère de l'Environnement du Québec. En cas de danger, appelez le 911.</p>
<h2>Quel chiffon garder sous la main</h2>
<p>Le t-shirt couleur à 32 $ le [pack] : absorbant et économique. Gardez un sac ouvert près des baies et des postes de vidange. La ratine est en rupture de stock pour le moment. Voir aussi les <a href="{{garage}}">chiffons de garage</a>.</p>""",
  "faq": [("Comment nettoyer de l'huile sur un plancher de garage?", "Contenez le déversement, absorbez-le avec des chiffons de l'extérieur vers le centre, dégraissez la tache restante et séchez. Mettez les chiffons imbibés dans un contenant métallique fermé."),
          ("Peut-on rincer l'huile vers le drain?", "Non. L'huile ne doit jamais aller dans un drain de plancher, un égout pluvial ou un fossé. Absorbez-la et faites éliminer les chiffons correctement."),
          ("Quoi faire des chiffons pleins d'huile?", "Les garder dans un contenant métallique fermé, puis les apporter à l'écocentre (particuliers) ou les faire collecter par une entreprise spécialisée (entreprises).")]},
 "en": {"path": "/en/guides/clean-up-oil-spill-with-rags/", "short": "Cleaning up an oil spill",
  "title": "How to clean up an oil spill in a garage with rags",
  "desc": "How to clean up an oil, fluid or fuel spill on a garage or shop floor with rags, step by step, and what to do with the soaked rags afterwards.",
  "eyebrow": "Guide · garages and shops", "h1": "Cleaning up an oil spill with rags",
  "lede": "An overflowing oil change, a tipped jug, a leak under a vehicle: here's how to clean up a small oil spill cleanly and safely.",
  "card": "Contain, absorb, clean, dispose: the steps for a small spill.", "alt": "Bags of coloured rags",
  "body": """<h2>Before you start</h2>
<ul><li><b>Stop the source</b>: stand the jug up, put a drain pan under the leak.</li>
<li><b>Remove ignition sources</b> if it's gasoline or a solvent: no flames, no sparks, ventilate.</li>
<li><b>Wear oil-resistant gloves</b> and check the product's safety data sheet (SDS).</li></ul>
<h2>The steps</h2>
<ol><li><b>Contain</b>: ring the spill with rags or an absorbent sock so it can't spread, especially towards a drain.</li>
<li><b>Absorb from the outside in</b> with <a href="{{p-tshirt-couleur}}">coloured T-shirt rags</a>. Lay them down, let them soak, lift them without scrubbing at first.</li>
<li><b>Put each soaked rag straight</b> into a closed metal container.</li>
<li><b>Degrease</b> the remaining stain with a floor degreaser, then wipe with clean rags.</li>
<li><b>Dry</b> the surface to prevent slips.</li></ol>
<h2>Don't</h2>
<ul><li><b>Never rinse oil towards a floor drain, storm sewer or ditch.</b></li>
<li>Don't leave soaked rags in a pile or an open trash can: see <a href="{{guide-huileux}}">oily rags and fire risk</a>.</li>
<li>Don't put oily rags in a washer or dryer.</li></ul>
<h2>After the cleanup</h2>
<p>Rags soaked with oil, fuel or coolant don't go in the regular trash. Households take them to an ecocentre; businesses have them collected by a specialized company. See <a href="{{guide-souilles}}">soiled rags at work</a>.</p>
<h2>Large spills</h2>
<p>Rags are for small indoor spills. For a large volume, or a leak that reaches soil, a waterway or a sewer, use a proper spill kit and report it to Urgence-Environnement at Québec's Ministry of the Environment. If there's danger, call 911.</p>
<h2>Which rag to keep handy</h2>
<p>Coloured T-shirt rags at $32 per [pack]: absorbent and economical. Keep an open bag near the bays and oil-change stations. Terry is out of stock for now. See also <a href="{{garage}}">garage shop rags</a>.</p>""",
  "faq": [("How do I clean oil off a garage floor?", "Contain the spill, absorb it with rags from the outside in, degrease the remaining stain and dry the floor. Put the soaked rags in a closed metal container."),
          ("Can I rinse oil down the drain?", "No. Oil must never go into a floor drain, storm sewer or ditch. Absorb it and have the rags disposed of properly."),
          ("What do I do with oil-soaked rags?", "Keep them in a closed metal container, then take them to an ecocentre (households) or have them collected by a specialized company (businesses).")]}}

GUIDE3_PAGES = P
GUIDE3_KEYS = list(P)
