"""Canada-wide pages: rag supplier for distributors outside Québec (user's terms: distributors only, 50 bags min, $28/$38, freight quoted) and reusable rags vs disposable cleaning wipes."""
WARE, BAGS = "entrepot-sacs-chiffons-blancs-et-couleur.webp", "sacs-chiffons-couleur-25-lb.webp"
PROV_FR = "Ontario, Nouveau-Brunswick, Nouvelle-Écosse, Île-du-Prince-Édouard, Terre-Neuve-et-Labrador, Manitoba, Saskatchewan, Alberta, Colombie-Britannique et les territoires"
PROV_EN = "Ontario, New Brunswick, Nova Scotia, Prince Edward Island, Newfoundland and Labrador, Manitoba, Saskatchewan, Alberta, British Columbia and the territories"
P = {}

P["canada"] = {"kind": "sector", "img": WARE, "rel": ["gros", "guide-lingettes", "livraison"],
 "fr": {"path": "/fournisseur-chiffons-recycles-canada/", "short": "Fournisseur de chiffons au Canada",
  "title": "Fournisseur de chiffons recyclés au Canada, en gros",
  "desc": "Chiffons recyclés en gros pour distributeurs partout au Canada : sacs de 25 lb à 28 $ couleur, 38 $ blanc dès 50 sacs, transport sur soumission.",
  "eyebrow": "Distributeurs · partout au Canada", "h1": "Fournisseur de chiffons recyclés en gros pour les distributeurs du Canada",
  "lede": "Entretien Laval (Chiffons ÉCO) fournit des chiffons d'essuyage en coton recyclé aux distributeurs de toutes les provinces : prix distributeur publié, minimum de 50 sacs, transport sur soumission.",
  "card": "Distributeurs hors Québec : 50 sacs minimum, 28 $ / 38 $, transport sur soumission.",
  "alt": "Entrepôt de sacs de chiffons recyclés blancs et couleur à Laval",
  "body": f"""<h2>Pour qui</h2>
<p>Distributeurs de produits sanitaires et d'entretien, fournisseurs industriels, de sécurité, de peinture et de soudage, quincailleries et centres de location situés ailleurs au Canada : {PROV_FR}. Hors Québec, nous vendons <b>aux distributeurs seulement</b>, pas aux utilisateurs finaux.</p>
<h2>Produits</h2>
<p>Chiffons d'essuyage (guenilles) en tissu de coton recyclé, lavés à l'eau chaude, triés, coupés et traités contre les punaises de lit, sans boutons ni fermetures éclair, emballés à Laval en sacs de 25 lb :</p>
<ul><li>T-shirt ou ratine de couleur : <b>28 $ le sac</b> (environ 1,12 $ la livre)</li>
<li>T-shirt ou ratine blanc : <b>38 $ le sac</b> (environ 1,52 $ la livre)</li></ul>
<h2>Conditions hors Québec</h2>
<ul><li><b>Minimum</b> : 50 sacs de 25 lb (1 250 lb) par commande; produits mélangés acceptés.</li>
<li><b>Prix</b> : 28 $ couleur, 38 $ blanc par sac, avant taxes.</li>
<li><b>Transport</b> : frais de transport sur soumission, selon la province et l'adresse de livraison.</li>
<li><b>Paiement</b> : commande confirmée et payée avant l'expédition.</li></ul>
<h2>Demander une soumission</h2>
<p>Écrivez à info@entretienlaval.ca ou utilisez le <a href="{{{{home#devis}}}}">formulaire</a> avec les produits, le nombre de sacs et l'adresse de livraison : nous répondons avec le prix du transport. La <a href="/docs/fiche-approvisionnement-responsable-chiffons-eco.pdf" download>fiche d'approvisionnement (PDF)</a> résume l'entreprise et les inscriptions fournisseur.</p>
<p>Au Québec, les conditions habituelles s'appliquent : voir <a href="{{{{gros}}}}">guenilles en gros</a> et <a href="{{{{livraison}}}}">livraison</a>.</p>""",
  "faq": [("Où trouver un fournisseur de chiffons recyclés au Canada?", "Entretien Laval (Chiffons ÉCO), à Laval (Québec), vend des chiffons d'essuyage en coton recyclé aux distributeurs de partout au Canada : sacs de 25 lb à 28 $ couleur et 38 $ blanc, dès 50 sacs, transport sur soumission."),
          ("Livrez-vous en Ontario, en Alberta ou en Colombie-Britannique?", "Oui, aux distributeurs, à partir de 50 sacs par commande. Les frais de transport sont calculés dans la soumission selon l'adresse."),
          ("Vendez-vous aux entreprises hors Québec qui ne sont pas des distributeurs?", "Non. Hors Québec, nous vendons seulement aux distributeurs et revendeurs, à partir de 50 sacs."),
          ("Vendez-vous des lingettes jetables?", "Non. Nous vendons des chiffons en coton recyclé réutilisables, une solution de rechange aux lingettes et au papier pour l'atelier et l'entretien.")]},
 "en": {"path": "/en/recycled-rag-supplier-canada/", "short": "Rag supplier in Canada",
  "title": "Recycled rag supplier in Canada, wholesale",
  "desc": "Canadian supplier of recycled wiping rags for distributors across Canada: 25 lb bags at $28 colored and $38 white from 50 bags, freight quoted per order.",
  "eyebrow": "Distributors · across Canada", "h1": "Wholesale recycled rag supplier for distributors across Canada",
  "lede": "Entretien Laval (ECO Rags) supplies recycled cotton wiping rags to distributors in every province: published distributor price, 50-bag minimum, freight quoted per order.",
  "card": "Distributors outside Québec: 50 bags minimum, $28 / $38, freight quoted.",
  "alt": "Warehouse of white and colored recycled rag bags in Laval",
  "body": f"""<h2>Who it's for</h2>
<p>Janitorial and sanitation distributors, industrial, safety, paint and welding suppliers, hardware stores and rental centres elsewhere in Canada: {PROV_EN}. Outside Québec we sell <b>to distributors only</b>, not to end users.</p>
<h2>Products</h2>
<p>Recycled cotton cloth wiping rags (shop rags), hot-water washed, sorted, cut and treated against bedbugs, with no buttons or zippers, packed in Laval in 25 lb bags:</p>
<ul><li>Colored T-shirt or terry: <b>$28 per bag</b> (about $1.12 per lb)</li>
<li>White T-shirt or terry: <b>$38 per bag</b> (about $1.52 per lb)</li></ul>
<h2>Terms outside Québec</h2>
<ul><li><b>Minimum</b>: 50 bags of 25 lb (1,250 lb) per order; mixed products accepted.</li>
<li><b>Price</b>: $28 colored, $38 white per bag, before tax.</li>
<li><b>Freight</b>: quoted per order, based on the province and delivery address.</li>
<li><b>Payment</b>: order confirmed and paid before shipping.</li></ul>
<h2>Request a quote</h2>
<p>Email info@entretienlaval.ca or use the <a href="{{{{home#devis}}}}">form</a> with the products, number of bags and delivery address: we reply with the freight price. The <a href="/docs/fiche-approvisionnement-responsable-chiffons-eco.pdf" download>supplier sheet (PDF)</a> sums up the company and its supplier registrations.</p>
<p>In Québec the usual terms apply: see <a href="{{{{gros}}}}">wholesale rags</a> and <a href="{{{{livraison}}}}">delivery</a>.</p>""",
  "faq": [("Where can I find a recycled rag supplier in Canada?", "Entretien Laval (ECO Rags) in Laval, Québec sells recycled cotton wiping rags to distributors across Canada: 25 lb bags at $28 colored and $38 white, from 50 bags, freight quoted per order."),
          ("Do you ship to Ontario, Alberta or British Columbia?", "Yes, to distributors, from 50 bags per order. Freight is calculated in the quote based on the address."),
          ("Do you sell to businesses outside Québec that are not distributors?", "No. Outside Québec we sell only to distributors and resellers, from 50 bags."),
          ("Do you sell disposable cleaning wipes?", "No. We sell reusable recycled cotton rags, an alternative to wipes and paper for shop and cleaning work.")]}}

P["guide-lingettes"] = {"kind": "guide", "img": BAGS, "rel": ["guide-papier", "canada", "couleur"],
 "fr": {"path": "/guides/chiffons-reutilisables-ou-lingettes-jetables/", "short": "Chiffons réutilisables ou lingettes jetables",
  "title": "Chiffons réutilisables ou lingettes jetables?",
  "desc": "Lingettes jetables ou chiffons en coton recyclé réutilisables : usages, coût au poids, déchets et sécurité, pour bien choisir en atelier.",
  "eyebrow": "Guide · comparer", "h1": "Chiffons en coton recyclé ou lingettes de nettoyage jetables?",
  "lede": "Les lingettes jetables servent une fois. Un chiffon en coton recyclé absorbe davantage et se lave s'il n'est pas imbibé d'huile ou de solvant.",
  "card": "Usages, coût, déchets : quand prendre un chiffon plutôt qu'une lingette.", "alt": "Sacs de chiffons recyclés de couleur",
  "body": """<h2>La différence</h2>
<p>Une lingette de nettoyage est un non-tissé jetable, souvent humidifié d'un produit. Un chiffon d'essuyage recyclé est un morceau de vrai tissu de coton (t-shirt ou ratine) récupéré, lavé et coupé.</p>
<h2>Quand le chiffon est le meilleur choix</h2>
<ul><li><b>Huile, graisse, liquides</b> : le coton, surtout la ratine, absorbe beaucoup.</li>
<li><b>Gros volumes</b> : en sac de 25 lb, vous payez au poids, environ 1,28 $ la livre en couleur (32 $ le sac avant taxes).</li>
<li><b>Moins de déchets</b> : les textiles récupérés évitent l'enfouissement, et un chiffon peu sale se relave. Voir <a href="{{guide-ranger}}">ranger, laver et réutiliser</a>.</li>
<li><b>Surfaces et outils</b> : le t-shirt blanc ne laisse pas de teinture et peu de peluches.</li></ul>
<h2>Quand garder les lingettes</h2>
<ul><li>Désinfection où le fabricant exige un produit précis et un temps de contact.</li>
<li>Hygiène des mains et situations où tout doit être jeté tout de suite.</li></ul>
<h2>Sécurité</h2>
<p>Un chiffon imbibé d'huile, de teinture ou de solvant peut s'enflammer seul : ne le mettez pas dans une sécheuse et rangez-le dans un contenant métallique fermé. Voir <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p>
<h2>Où acheter</h2>
<p>Au Québec, commandez nos <a href="{{couleur}}">chiffons couleur</a> ou <a href="{{blancs}}">blancs</a>. Ailleurs au Canada, nous fournissons les distributeurs : voir <a href="{{canada}}">fournisseur de chiffons au Canada</a>.</p>""",
  "faq": [("Les chiffons recyclés remplacent-ils les lingettes de nettoyage?", "Pour l'essuyage d'huile, de graisse, de liquides et le nettoyage courant en atelier, oui. Pour une désinfection avec un produit et un temps de contact précis, suivez les directives du fabricant."),
          ("Combien coûtent les chiffons recyclés au poids?", "Chez Entretien Laval, 32 $ le sac de 25 lb en couleur (environ 1,28 $ la livre) et 42 $ en blanc, avant taxes. Distributeurs : 28 $ / 38 $ dès 50 sacs.")]},
 "en": {"path": "/en/guides/reusable-rags-vs-cleaning-wipes/", "short": "Reusable rags vs cleaning wipes",
  "title": "Reusable rags vs disposable cleaning wipes",
  "desc": "Disposable cleaning wipes or reusable recycled cotton rags: uses, cost per pound, waste and safety, to choose for shop and cleaning work.",
  "eyebrow": "Guide · comparing", "h1": "Recycled cotton rags or disposable cleaning wipes?",
  "lede": "Disposable wipes are used once. A recycled cotton rag absorbs more and can be washed if it isn't soaked with oil or solvent.",
  "card": "Uses, cost, waste: when to pick a rag over a wipe.", "alt": "Bags of colored recycled rags",
  "body": """<h2>The difference</h2>
<p>A cleaning wipe is a disposable nonwoven sheet, often pre-moistened with a product. A recycled wiping rag is a piece of real cotton cloth (T-shirt or terry), reclaimed, washed and cut.</p>
<h2>When a rag is the better choice</h2>
<ul><li><b>Oil, grease, liquids</b>: cotton, especially terry, holds a lot.</li>
<li><b>High volume</b>: in 25 lb bags you pay by weight, about $1.28 per lb for colored ($32 per bag before tax).</li>
<li><b>Less waste</b>: reclaimed textiles stay out of landfill, and a lightly soiled rag can be washed again. See <a href="{{guide-ranger}}">store, wash and reuse</a>.</li>
<li><b>Surfaces and tools</b>: white T-shirt leaves no dye and little lint.</li></ul>
<h2>When to keep wipes</h2>
<ul><li>Disinfection where the manufacturer requires a specific product and contact time.</li>
<li>Hand hygiene and situations where everything must be thrown out right away.</li></ul>
<h2>Safety</h2>
<p>A rag soaked with oil, stain or solvent can ignite on its own: never put it in a dryer, and keep it in a closed metal container. See <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p>
<h2>Where to buy</h2>
<p>In Québec, order our <a href="{{couleur}}">colored</a> or <a href="{{blancs}}">white</a> rags. Elsewhere in Canada we supply distributors: see <a href="{{canada}}">rag supplier in Canada</a>.</p>""",
  "faq": [("Can recycled rags replace cleaning wipes?", "For wiping oil, grease, liquids and everyday shop cleaning, yes. For disinfection that needs a specific product and contact time, follow the manufacturer's directions."),
          ("How much do recycled rags cost per pound?", "At Entretien Laval, $32 per 25 lb bag colored (about $1.28 per lb) and $42 white, before tax. Distributors: $28 / $38 from 50 bags.")]}}

CANADA_PAGES = P
