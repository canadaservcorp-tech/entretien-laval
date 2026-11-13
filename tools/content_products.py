# One page per product (4 products x FR/EN).
DELIV_FR = "<h2>Livraison et commande</h2><p>Livré à votre adresse : Laval 15 $ dès 1 sac, Montréal 25 $ dès 2 sacs. Ailleurs au Québec, minimum 1 000 lb (40 sacs). Ramassage à Laval possible. Voir <a href=\"{{livraison}}\">la livraison</a> ou <a href=\"{{home#devis}}\">demandez une soumission</a>.</p>"
DELIV_EN = "<h2>Delivery and ordering</h2><p>Delivered to your address: Laval $15 from 1 bag, Montréal $25 from 2 bags. Elsewhere in Québec, 1,000 lb minimum (40 bags). Pickup in Laval available. See <a href=\"{{livraison}}\">delivery</a> or <a href=\"{{home#devis}}\">request a quote</a>.</p>"
QUAL_FR = "<h2>Qualité</h2><p>Coton recyclé, lavé à l'eau chaude, traité contre les punaises de lit, sans métal, boutons ni fermetures éclair, coupé et emballé à Laval en sacs de 25 lb.</p>"
QUAL_EN = "<h2>Quality</h2><p>Recycled cotton, washed in hot water, treated against bedbugs, with metal, buttons and zippers removed, cut and packed in Laval in 25 lb bags.</p>"

SPEC = [
 # key, product id, img, price, rel, fr(path, name, eyebrow, lede, uses, body), en(...)
 ("p-tshirt-couleur", "tshirt-couleur", "sac-chiffons-t-shirt-couleur-25-lb.webp", 32, ["p-ratine-couleur", "garage", "construction"],
  ("/chiffons-t-shirt-couleur/", "Chiffons t-shirt couleur", "T-shirt couleur",
   "Guenilles en jersey de coton couleur, douces et absorbantes : notre produit le plus vendu pour l'essuyage de tous les jours.",
   "<li><b>Garages et mécanique</b> : mains, outils, jauges, fuites légères.</li><li><b>Ateliers et usines</b> : essuyage des machines et des établis.</li><li><b>Chantiers</b> : nettoyage d'outils, de coffrages et de surfaces.</li><li><b>Entretien ménager</b> : poussière, vitres, surfaces.</li>",
   "<p>Le t-shirt (jersey) est mince et souple. Il épouse les pièces, ne raye pas et absorbe bien l'eau, l'huile légère et les liquides de nettoyage. Pour l'huile en grande quantité, prenez la <a href=\"{{p-ratine-couleur}}\">ratine couleur</a>; pour la peinture, le <a href=\"{{p-tshirt-blanc}}\">t-shirt blanc</a>.</p>",
   [("Le t-shirt couleur peut-il déteindre?", "Avec des solvants, de la teinture ou du vernis, un tissu teint peut déteindre. Pour ces usages, choisissez le t-shirt blanc."),
    ("Quelle taille ont les morceaux?", "Ils sont coupés en morceaux prêts à utiliser, faciles à tenir en main. La taille varie selon le vêtement d'origine.")]),
  ("/en/colored-t-shirt-rags/", "Colored T-shirt rags", "Colored T-shirt",
   "Colored cotton jersey shop rags, soft and absorbent: our best seller for everyday wiping.",
   "<li><b>Garages and mechanics</b>: hands, tools, dipsticks, small leaks.</li><li><b>Shops and plants</b>: wiping machines and workbenches.</li><li><b>Job sites</b>: cleaning tools, forms and surfaces.</li><li><b>Janitorial</b>: dust, windows, surfaces.</li>",
   "<p>T-shirt (jersey) is thin and flexible. It follows the part, doesn't scratch and absorbs water, light oil and cleaning liquids well. For large amounts of oil, take <a href=\"{{p-ratine-couleur}}\">colored terry</a>; for paint, <a href=\"{{p-tshirt-blanc}}\">white T-shirt</a>.</p>",
   [("Can colored T-shirt rags bleed?", "With solvents, stain or varnish, dyed fabric can bleed. For those jobs, choose white T-shirt rags."),
    ("How big are the pieces?", "They are cut into ready-to-use, hand-sized pieces. Size varies with the original garment.")])),
 ("p-ratine-couleur", "ratine-couleur", "chiffon-garagiste-huile-mains.webp", 32, ["p-tshirt-couleur", "garage", "industrie"],
  ("/chiffons-ratine-couleur/", "Chiffons ratine couleur", "Ratine couleur",
   "Guenilles en tissu éponge couleur, épaisses et très résistantes : pour l'huile, la graisse et les gros déversements.",
   "<li><b>Garages et machinerie lourde</b> : huile, graisse, liquide de refroidissement.</li><li><b>Usinage et soudure</b> : huile de coupe, pièces grasses.</li><li><b>Fermes et transport</b> : équipement, camions, hydraulique.</li><li><b>Déversements</b> : absorber vite un gros volume de liquide.</li>",
   "<p>La ratine (tissu éponge, comme une serviette) a des boucles qui retiennent beaucoup plus de liquide que le t-shirt. Elle résiste au frottement sur les surfaces rugueuses et se réutilise plusieurs fois. Pour l'essuyage léger, le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> suffit.</p>",
   [("La ratine laisse-t-elle des peluches?", "Un peu plus que le t-shirt. Pour les surfaces qui doivent rester sans peluches, prenez le t-shirt."),
    ("Que faire des chiffons pleins d'huile?", "Rangez-les dans un contenant métallique fermé : voir notre guide <a href=\"{{guide-huileux}}\">chiffons huileux et risque d'incendie</a>.")]),
  ("/en/colored-terry-rags/", "Colored terry rags", "Colored terry",
   "Colored terry towel rags, thick and very tough: for oil, grease and big spills.",
   "<li><b>Garages and heavy equipment</b>: oil, grease, coolant.</li><li><b>Machining and welding</b>: cutting oil, greasy parts.</li><li><b>Farms and trucking</b>: equipment, trucks, hydraulics.</li><li><b>Spills</b>: soak up a large volume of liquid fast.</li>",
   "<p>Terry (towel cloth) has loops that hold far more liquid than T-shirt. It stands up to rubbing on rough surfaces and can be reused several times. For light wiping, <a href=\"{{p-tshirt-couleur}}\">colored T-shirt</a> is enough.</p>",
   [("Does terry leave lint?", "A little more than T-shirt. For surfaces that must stay lint-free, choose T-shirt."),
    ("What do I do with oily rags?", "Store them in a closed metal container: see our guide <a href=\"{{guide-huileux}}\">oily rags and fire risk</a>.")])),
 ("p-tshirt-blanc", "tshirt-blanc", "sacs-chiffons-blancs-25-lb.webp", 42, ["p-ratine-blanc", "peinture", "industrie"],
  ("/chiffons-t-shirt-blanc/", "Chiffons t-shirt blanc", "T-shirt blanc",
   "Chiffons d'essuyage en jersey de coton blanc, sans transfert de couleur : peinture, teinture, vernis et surfaces délicates.",
   "<li><b>Peinture et finition</b> : teinture, vernis, laque, retouches.</li><li><b>Ébénisterie</b> : appliquer et essuyer l'huile et la teinture.</li><li><b>Imprimerie</b> : nettoyage des presses et des rouleaux.</li><li><b>Inox et surfaces claires</b> : cuisines, comptoirs, vitres.</li>",
   "<p>Le blanc ne déteint pas avec les solvants et montre la saleté. Le jersey mince donne une finition uniforme, sans laisser de marques. Pour les gros surplus de liquide, prenez la <a href=\"{{p-ratine-blanc}}\">ratine blanche</a>.</p>",
   [("Les chiffons t-shirt blancs sont-ils 100 % blancs?", "Ils sont triés pour ne garder que des textiles blancs ou très pâles, sans transfert de couleur."),
    ("Conviennent-ils au vernis et à la laque?", "Oui. Le jersey blanc mince laisse peu de peluches et ne transfère pas de couleur.")]),
  ("/en/white-t-shirt-rags/", "White T-shirt rags", "White T-shirt",
   "White cotton jersey wiping rags with no color transfer: paint, stain, varnish and delicate surfaces.",
   "<li><b>Painting and finishing</b>: stain, varnish, lacquer, touch-ups.</li><li><b>Woodworking</b>: applying and wiping oil and stain.</li><li><b>Printing</b>: cleaning presses and rollers.</li><li><b>Stainless and light surfaces</b>: kitchens, counters, windows.</li>",
   "<p>White doesn't bleed with solvents and shows the dirt. Thin jersey gives an even finish without leaving marks. For heavy liquid, take <a href=\"{{p-ratine-blanc}}\">white terry</a>.</p>",
   [("Are white T-shirt rags 100% white?", "They are sorted to keep only white or very pale textiles, with no color transfer."),
    ("Are they good for varnish and lacquer?", "Yes. Thin white jersey leaves little lint and transfers no color.")])),
 ("p-ratine-blanc", "ratine-blanc", "chiffon-ratine-blanc-moteur.webp", 42, ["p-tshirt-blanc", "peinture", "restauration"],
  ("/chiffons-ratine-blanc/", "Chiffons ratine blanc", "Ratine blanche",
   "Guenilles en tissu éponge blanc de qualité supérieure : très absorbantes, sans transfert de couleur.",
   "<li><b>Esthétique automobile et lave-auto</b> : séchage, cire, intérieur.</li><li><b>Restaurants et cuisines</b> : déversements, inox, équipement.</li><li><b>Peinture</b> : gros surplus, nettoyage d'outils.</li><li><b>Mécanique fine</b> : voir l'huile et les fuites sur un tissu blanc.</li>",
   "<p>La ratine blanche combine l'absorption du tissu éponge et l'absence de couleur. C'est le chiffon le plus polyvalent : il absorbe comme une serviette et ne laisse aucune trace de teinture. Pour l'essuyage fin, prenez le <a href=\"{{p-tshirt-blanc}}\">t-shirt blanc</a>.</p>",
   [("Pourquoi la ratine blanche coûte-t-elle plus cher?", "Le tri des textiles blancs est plus long et le blanc est plus rare. Elle coûte 42 $ le sac, contre 32 $ pour la couleur."),
    ("Puis-je avoir un échantillon?", "Oui, sur demande.")]),
  ("/en/white-terry-rags/", "White terry rags", "White terry",
   "Premium white terry towel rags: very absorbent, with no color transfer.",
   "<li><b>Auto detailing and car washes</b>: drying, wax, interiors.</li><li><b>Restaurants and kitchens</b>: spills, stainless, equipment.</li><li><b>Painting</b>: heavy excess, tool cleaning.</li><li><b>Precision mechanics</b>: see oil and leaks on a white cloth.</li>",
   "<p>White terry combines towel-cloth absorbency with no color. It is the most versatile rag: it soaks up like a towel and leaves no dye. For fine wiping, take <a href=\"{{p-tshirt-blanc}}\">white T-shirt</a>.</p>",
   [("Why does white terry cost more?", "Sorting white textiles takes longer and white is rarer. It is $42 per bag, against $32 for colored."),
    ("Can I get a sample?", "Yes, on request.")])),
]

def _page(lang, d, price):
    path, name, short, lede, uses, body, faq = d
    fr = lang == "fr"
    kw = ("guenilles, chiffons d'essuyage et linges recyclés" if fr else "wiping rags and shop rags")
    p = f"{price} $" if fr else f"${price}"
    return {"path": path, "short": short,
     "title": (f"{name} 25 lb, {p} | Guenilles Laval" if fr else f"{name}, 25 lb bag, {p} | Laval | ECO Rags"),
     "desc": (f"{name} en coton recyclé, lavés et traités anti-punaises. {p} le sac de 25 lb avant taxes. Livraison à Laval et Montréal." if fr
              else f"{name} in recycled cotton, washed and bedbug-treated. {p} per 25 lb bag before tax. Delivery in Laval and Montréal."),
     "eyebrow": ("Produit · " if fr else "Product · ") + short.lower(), "h1": (f"{name} : {p} le sac de 25 lb" if fr else f"{name}: {p} per 25 lb bag"),
     "lede": lede + (f" Lavés et traités anti-punaises, {p} le [pack]." if fr else f" Washed and bedbug-treated, {p} per [pack]."),
     "card": lede.split(":")[0] + (f". {p} le [pack]." if fr else f". {p} per [pack]."),
     "alt": name + (" en sac de 25 lb" if fr else ", 25 lb bag"),
     "body": (f"<h2>Usages</h2><ul>{uses}</ul><h2>Pourquoi ce chiffon</h2>" if fr else f"<h2>Uses</h2><ul>{uses}</ul><h2>Why this rag</h2>") + body
             + (QUAL_FR if fr else QUAL_EN) + (DELIV_FR if fr else DELIV_EN)
             + (f"<p>Aussi appelés {kw} : un seul type par sac, {p} avant taxes, facture avec TPS et TVQ.</p>" if fr else f"<p>Also called {kw}: one type per bag, {p} before tax, invoiced with GST and QST.</p>"),
     "faq": faq}

PRODUCT_PAGES = {}
PRODUCT_PAGE_OF = {}
for key, pid, img, price, rel, fr, en in SPEC:
    PRODUCT_PAGES[key] = {"kind": "product", "img": img, "products": [pid], "rel": rel, "fr": _page("fr", fr, price), "en": _page("en", en, price)}
    PRODUCT_PAGE_OF[pid] = key
