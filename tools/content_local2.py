"""Local pages: Laval neighbourhoods and North/South Shore towns inside the online delivery zones.

Every fee, minimum and price comes from content_order.CHECKOUT (the same data the checkout uses), so these pages
can never promise a delivery the checkout refuses. Each page has its own intro, uses, example order and FAQ.
"""
import content_order as O

BAG, BAGS, BALE, SHOP, WHITE = ("sac-chiffons-t-shirt-couleur-25-lb.webp", "sacs-chiffons-couleur-25-lb.webp",
    "balle-compressee-de-chiffons-eco-en-textiles-recyc.webp", "sac-de-chiffons-d-atelier-conditionnes-prets-a-l-u.webp",
    "sacs-chiffons-blancs-25-lb.webp")

PRICE = {"tshirt-couleur": 32, "tshirt-blanc": 42}
NAME = {"fr": {"tshirt-couleur": "t-shirt couleur", "tshirt-blanc": "t-shirt blanc"},
        "en": {"tshirt-couleur": "coloured T-shirt", "tshirt-blanc": "white T-shirt"}}
ZONES = {z["id"]: z for z in O.CHECKOUT["zones"]}
PICKUP = O.CHECKOUT["pickup"]["address"]
DAYS = O.DAYS
ZONE_NAME = {"laval": ("Laval", "Laval"), "rive-nord": ("Rive-Nord", "North Shore"), "rive-sud": ("Rive-Sud", "South Shore")}

L = []  # one dict per page

# ---------------- Laval neighbourhoods (zone Laval) ----------------
L.append(dict(key="ville-chomedey", name="Chomedey", zone="laval", img=BAG,
 fr="/chiffons-guenilles-chomedey/", en="/en/rags-chomedey/", rel=["carrosserie", "p-tshirt-couleur", "guide-garage-mois"],
 title_fr="Chiffons et guenilles à Chomedey (Laval) – livraison 15 $",
 desc_fr="Guenilles recyclées livrées à Chomedey : sac de 25 lb, t-shirt couleur 32 $ ou blanc 42 $, livraison 15 $ dès 1 sac ou ramassage gratuit à Laval.",
 title_en="Shop rags in Chomedey, Laval – $15 delivery",
 desc_en="Recycled cotton rags delivered in Chomedey: 25 lb bag, coloured T-shirt $32 or white $42, $15 delivery from 1 bag, or free pickup in Laval.",
 intro_fr="Chomedey est l'un des grands quartiers de Laval. Le long de ses boulevards commerciaux, comme Curé-Labelle, Chomedey et Saint-Martin, on trouve beaucoup d'entreprises de l'automobile : garages, ateliers de mécanique, carrosseries et concessionnaires. Ce sont les entreprises qui passent le plus de chiffons, chaque jour.",
 intro_en="Chomedey is one of Laval's large districts. Along its commercial boulevards, such as Curé-Labelle, Chomedey and Saint-Martin, there are many automotive businesses: garages, repair shops, body shops and dealerships. They go through more rags than anyone, every day.",
 uses_h_fr="Pour les garages et ateliers de Chomedey", uses_h_en="For Chomedey garages and shops",
 uses_fr=[("Mécanique", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> pour les mains, les outils, les jauges et les pièces. Voir <a href=\"{{garage}}\">chiffons de garage</a>."),
          ("Carrosserie et préparation", "le <a href=\"{{p-tshirt-blanc}}\">t-shirt blanc</a> pour dégraisser avant la peinture, sans transfert de couleur. Voir <a href=\"{{carrosserie}}\">chiffons de carrosserie</a>."),
          ("Déversements au plancher", "plusieurs chiffons couleur pour absorber l'huile, puis un contenant métallique fermé. Voir <a href=\"{{guide-deversement}}\">nettoyer un déversement d'huile</a>.")],
 uses_en=[("Mechanics", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags for hands, tools, dipsticks and parts. See <a href=\"{{garage}}\">garage rags</a>."),
          ("Body work and prep", "<a href=\"{{p-tshirt-blanc}}\">white T-shirt</a> rags to degrease before paint, with no colour transfer. See <a href=\"{{carrosserie}}\">auto body rags</a>."),
          ("Floor spills", "several coloured rags to soak up oil, then a closed metal container. See <a href=\"{{guide-deversement}}\">cleaning up an oil spill</a>.")],
 ex=[("tshirt-couleur", 4), ("tshirt-blanc", 1)],
 ex_fr="Un garage de Chomedey qui prend 4 sacs de t-shirt couleur pour l'atelier et 1 sac de t-shirt blanc pour la carrosserie",
 ex_en="A Chomedey garage taking 4 bags of coloured T-shirt rags for the shop and 1 bag of white T-shirt rags for body work",
 guides=["guide-garage-mois", "guide-deversement", "guide-huileux"],
 faq_fr=[("Quel chiffon pour un garage de Chomedey?", "Le t-shirt couleur à 32 $ le [pack] pour la mécanique courante, et quelques sacs de t-shirt blanc à 42 $ pour la carrosserie et les surfaces peintes."),
         ("Avez-vous de la ratine pour l'huile?", "La ratine (couleur et blanche) est en rupture de stock pour le moment. Le t-shirt couleur absorbe bien l'huile et la graisse courantes; prenez-en quelques morceaux de plus pour un gros dégât.")],
 faq_en=[("Which rag for a garage in Chomedey?", "Coloured T-shirt rags at $32 per [pack] for everyday mechanics, plus a few bags of white T-shirt rags at $42 for body work and painted surfaces."),
         ("Do you have terry for oil?", "Terry (coloured and white) is out of stock for now. Coloured T-shirt rags handle everyday oil and grease well; use a few extra pieces for a big spill.")]))

L.append(dict(key="ville-laval-des-rapides", name="Laval-des-Rapides", zone="laval", img=BAGS,
 fr="/chiffons-guenilles-laval-des-rapides/", en="/en/rags-laval-des-rapides/", rel=["entretien", "restauration", "guide-vitres"],
 title_fr="Chiffons de nettoyage à Laval-des-Rapides – livraison 15 $",
 desc_fr="Chiffons recyclés pour l'entretien d'immeubles, de bureaux et de restaurants à Laval-des-Rapides : sac de 25 lb dès 32 $, livré pour 15 $ dès 1 sac.",
 title_en="Cleaning rags in Laval-des-Rapides – $15 delivery",
 desc_en="Recycled rags for building, office and restaurant cleaning in Laval-des-Rapides: 25 lb bag from $32, delivered for $15 from 1 bag.",
 intro_fr="Laval-des-Rapides, au sud de l'île Jésus près de la rivière des Prairies, est un quartier dense : immeubles à logements, bureaux, commerces et restaurants. Ici, les chiffons servent surtout à l'entretien : halls, cuisines, salles mécaniques et ménage après travaux.",
 intro_en="Laval-des-Rapides, in the south of Île Jésus near the Rivière des Prairies, is a dense district: apartment buildings, offices, shops and restaurants. Here, rags are mostly used for cleaning: lobbies, kitchens, mechanical rooms and post-renovation cleanup.",
 uses_h_fr="Pour l'entretien des immeubles et des commerces", uses_h_en="For building and business cleaning",
 uses_fr=[("Concierges et entretien ménager", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> pour la poussière, les surfaces et l'équipement. Voir <a href=\"{{entretien}}\">entretien ménager</a>."),
          ("Vitres, miroirs et inox des halls", "le <a href=\"{{p-tshirt-blanc}}\">t-shirt blanc</a>, mince et peu pelucheux. Voir <a href=\"{{guide-vitres}}\">chiffons pour vitres et inox</a>."),
          ("Restaurants", "couleur pour la graisse des hottes et les planchers, blanc pour l'inox. Voir <a href=\"{{restauration}}\">restaurants et cuisines</a>.")],
 uses_en=[("Custodians and cleaning crews", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags for dust, surfaces and equipment. See <a href=\"{{entretien}}\">janitorial rags</a>."),
          ("Lobby glass, mirrors and stainless", "<a href=\"{{p-tshirt-blanc}}\">white T-shirt</a> rags, thin and low-lint. See <a href=\"{{guide-vitres}}\">rags for glass and stainless steel</a>."),
          ("Restaurants", "coloured for hood grease and floors, white for stainless steel. See <a href=\"{{restauration}}\">restaurants and kitchens</a>.")],
 ex=[("tshirt-couleur", 2), ("tshirt-blanc", 1)],
 ex_fr="Un concierge qui entretient quelques immeubles et prend 2 sacs de t-shirt couleur pour le ménage et 1 sac de t-shirt blanc pour les vitres et l'inox",
 ex_en="A custodian looking after a few buildings who takes 2 bags of coloured T-shirt rags for cleaning and 1 bag of white T-shirt rags for glass and stainless",
 guides=["guide-vitres", "guide-papier", "guide-ranger"],
 faq_fr=[("Pouvez-vous livrer un immeuble chaque mois?", "Oui. Choisissez la quantité et le rythme (toutes les 2 semaines ou chaque mois) et nous livrons au même prix, avec facture."),
         ("Quel chiffon pour l'inox d'un hall ou d'une cuisine?", "Le t-shirt blanc : il ne déteint pas et laisse peu de peluches. Essuyez dans le sens du grain de l'inox.")],
 faq_en=[("Can you deliver to a building every month?", "Yes. Choose the quantity and schedule (every 2 weeks or every month) and we deliver at the same price, with an invoice."),
         ("Which rag for lobby or kitchen stainless steel?", "White T-shirt rags: they don't bleed and leave little lint. Wipe with the grain of the steel.")]))

L.append(dict(key="ville-sainte-rose", name="Sainte-Rose", zone="laval", img=WHITE,
 fr="/chiffons-guenilles-sainte-rose/", en="/en/rags-sainte-rose/", rel=["peinture", "ebenisterie", "p-tshirt-blanc"],
 title_fr="Chiffons blancs à Sainte-Rose, Laval : peinture et teinture",
 desc_fr="Chiffons de coton blanc pour peintres, ébénistes et rénovation à Sainte-Rose (Laval) : 42 $ le sac de 25 lb, livraison 15 $ dès 1 sac ou ramassage gratuit.",
 title_en="White rags in Sainte-Rose, Laval: painting and staining",
 desc_en="White cotton rags for painters, woodworkers and renovators in Sainte-Rose, Laval: $42 per 25 lb bag, $15 delivery from 1 bag, or free pickup.",
 intro_fr="Sainte-Rose, dans le nord de Laval au bord de la rivière des Mille Îles, est surtout résidentiel, avec le Vieux-Sainte-Rose et ses maisons anciennes. Les entreprises qui y travaillent sont souvent des peintres, des entrepreneurs en rénovation et des ébénistes : des métiers où le chiffon blanc compte.",
 intro_en="Sainte-Rose, in the north of Laval on the Rivière des Mille Îles, is mostly residential, with Vieux-Sainte-Rose and its older homes. The businesses working there are often painters, renovation contractors and woodworkers: trades where a white rag matters.",
 uses_h_fr="Pour la peinture, la teinture et la rénovation", uses_h_en="For painting, staining and renovation",
 uses_fr=[("Teinture, vernis, huile", "le <a href=\"{{p-tshirt-blanc}}\">t-shirt blanc</a>, sans transfert de couleur sur le bois. Voir <a href=\"{{guide-teinture}}\">quel chiffon pour teindre le bois</a>."),
          ("Nettoyage des pinceaux et des outils", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a>, moins cher, quand la couleur n'a pas d'importance."),
          ("Diluants et solvants", "du blanc, pour éviter que la teinture d'un tissu coloré déteigne. Voir <a href=\"{{guide-solvants}}\">chiffons et solvants</a>.")],
 uses_en=[("Stain, varnish, oil", "<a href=\"{{p-tshirt-blanc}}\">white T-shirt</a> rags, with no colour transfer on wood. See <a href=\"{{guide-teinture}}\">best rag for staining wood</a>."),
          ("Cleaning brushes and tools", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags, cheaper, when colour doesn't matter."),
          ("Thinners and solvents", "white, so the dye of a coloured fabric can't bleed. See <a href=\"{{guide-solvants}}\">rags and solvents</a>.")],
 ex=[("tshirt-blanc", 2)],
 ex_fr="Un peintre de Sainte-Rose qui prend 2 sacs de t-shirt blanc pour un chantier de teinture",
 ex_en="A Sainte-Rose painter taking 2 bags of white T-shirt rags for a staining job",
 guides=["guide-teinture", "guide-huileux", "guide-solvants"],
 faq_fr=[("Quel chiffon pour teindre une galerie ou des boiseries?", "Le t-shirt blanc : mince, peu pelucheux et sans transfert de couleur. Après usage, étendez les chiffons imbibés d'huile ou de teinture à plat dehors, ou gardez-les dans un contenant métallique fermé avec de l'eau."),
         ("Puis-je ramasser un seul sac?", f"Oui, gratuitement, au {PICKUP}. Commandez en ligne en choisissant « Ramassage » : nous vous écrivons quand c'est prêt.")],
 faq_en=[("Which rag for staining a deck or wood trim?", "White T-shirt rags: thin, low-lint and no colour transfer. After use, lay oil- or stain-soaked rags flat outdoors, or keep them in a closed metal container with water."),
         ("Can I pick up a single bag?", f"Yes, for free, at {PICKUP}. Order online and choose “Pickup”: we email you when it's ready.")]))

L.append(dict(key="ville-vimont", name="Vimont", zone="laval", img=BALE,
 fr="/chiffons-guenilles-vimont/", en="/en/rags-vimont/", rel=["plomberie-cvac", "construction", "guide-souilles"],
 title_fr="Guenilles à Vimont (Laval) pour plombiers et entrepreneurs",
 desc_fr="Guenilles recyclées pour plombiers, électriciens, frigoristes et entrepreneurs de Vimont : sac de 25 lb à 32 $, livré pour 15 $ dès 1 sac, ou ramassage gratuit.",
 title_en="Shop rags in Vimont, Laval for plumbers and contractors",
 desc_en="Recycled rags for plumbers, electricians, HVAC techs and contractors in Vimont, Laval: $32 per 25 lb bag, $15 delivery from 1 bag, or free pickup.",
 intro_fr="Vimont, au centre-nord de Laval, compte beaucoup d'entrepreneurs qui travaillent à partir de leur camion : plombiers, électriciens, frigoristes, techniciens en chauffage et en climatisation. Pour eux, le bon réflexe est d'avoir un sac de chiffons dans chaque véhicule.",
 intro_en="Vimont, in north-central Laval, is home to many contractors who work out of their trucks: plumbers, electricians, refrigeration and HVAC technicians. For them, the habit that pays off is keeping a bag of rags in every vehicle.",
 uses_h_fr="Pour les entrepreneurs et les camions de service", uses_h_en="For contractors and service trucks",
 uses_fr=[("Plomberie et CVAC", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> pour les raccords, la pâte à joint, l'huile de compresseur et les mains. Voir <a href=\"{{plomberie-cvac}}\">plomberie et CVAC</a>."),
          ("Chez le client", "un chiffon propre sous un raccord protège les planchers et les finis pendant la réparation."),
          ("Chiffons souillés", "un contenant métallique fermé dans le camion, vidé régulièrement. Voir <a href=\"{{guide-souilles}}\">chiffons souillés en entreprise</a>.")],
 uses_en=[("Plumbing and HVAC", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags for fittings, pipe dope, compressor oil and hands. See <a href=\"{{plomberie-cvac}}\">plumbing and HVAC</a>."),
          ("At the customer's", "a clean rag under a fitting protects floors and finishes during the repair."),
          ("Dirty rags", "a closed metal container in the truck, emptied regularly. See <a href=\"{{guide-souilles}}\">soiled rags at work</a>.")],
 ex=[("tshirt-couleur", 3)],
 ex_fr="Une entreprise de plomberie de Vimont qui met un sac de t-shirt couleur dans chacun de ses 3 camions",
 ex_en="A Vimont plumbing company putting a bag of coloured T-shirt rags in each of its 3 trucks",
 guides=["guide-souilles", "guide-garage-mois", "guide-solvants"],
 faq_fr=[("Livrez-vous à une adresse résidentielle?", "Oui, à l'adresse de votre choix : maison, bureau, entrepôt ou chantier. La livraison à Laval coûte 15 $ par commande, dès 1 sac."),
         ("Combien de sacs pour une équipe de techniciens?", "Commencez par un sac par camion, notez combien de semaines il dure, puis utilisez notre calculateur pour planifier une commande mensuelle.")],
 faq_en=[("Do you deliver to a home address?", "Yes, to any address you choose: home, office, warehouse or job site. Delivery in Laval is $15 per order, from 1 bag."),
         ("How many bags for a team of technicians?", "Start with one bag per truck, note how many weeks it lasts, then use our calculator to plan a monthly order.")]))

L.append(dict(key="ville-fabreville", name="Fabreville", zone="laval", img=BALE,
 fr="/chiffons-guenilles-fabreville/", en="/en/rags-fabreville/", rel=["guide-deversement", "p-tshirt-couleur", "commander"],
 title_fr="Guenilles à Fabreville (Laval) : flottes, équipement, déneigement",
 desc_fr="Guenilles recyclées pour flottes de véhicules, déneigement et entretien d'équipement à Fabreville : 32 $ le sac de 25 lb, livraison 15 $ ou ramassage gratuit.",
 title_en="Shop rags in Fabreville, Laval: fleets, equipment, snow removal",
 desc_en="Recycled rags for vehicle fleets, snow removal and equipment maintenance in Fabreville, Laval: $32 per 25 lb bag, $15 delivery or free pickup.",
 intro_fr="Fabreville, dans l'ouest de Laval, accueille des entreprises qui entretiennent elles-mêmes leur équipement : transporteurs, entrepreneurs en déneigement et en aménagement paysager, propriétaires de petites flottes. Avant chaque saison, on vérifie les moteurs, l'hydraulique et les graisseurs : beaucoup d'essuyage.",
 intro_en="Fabreville, in western Laval, has businesses that maintain their own equipment: carriers, snow removal and landscaping contractors, small fleet owners. Before each season, engines, hydraulics and grease fittings get checked: lots of wiping.",
 uses_h_fr="Pour l'entretien des véhicules et de l'équipement", uses_h_en="For vehicle and equipment maintenance",
 uses_fr=[("Moteurs, hydraulique, graisseurs", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a>, le plus économique. Voir <a href=\"{{camions}}\">camions lourds et flottes</a>."),
          ("Déversements d'huile ou de carburant", "absorbez avec des chiffons, jamais vers un drain. Voir <a href=\"{{guide-deversement}}\">nettoyer un déversement d'huile</a>."),
          ("Gros volumes", "plus de 10 sacs : demandez une soumission. Voir <a href=\"{{guide-entreprise}}\">acheter des guenilles en gros pour une entreprise</a>.")],
 uses_en=[("Engines, hydraulics, grease fittings", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags, the most economical. See <a href=\"{{camions}}\">heavy trucks and fleets</a>."),
          ("Oil or fuel spills", "soak them up with rags, never towards a drain. See <a href=\"{{guide-deversement}}\">cleaning up an oil spill</a>."),
          ("Large volumes", "more than 10 bags: request a quote. See <a href=\"{{guide-entreprise}}\">buying rags in bulk for a business</a>.")],
 ex=[("tshirt-couleur", 6)],
 ex_fr="Un entrepreneur en déneigement de Fabreville qui prend 6 sacs de t-shirt couleur avant la saison",
 ex_en="A Fabreville snow removal contractor taking 6 bags of coloured T-shirt rags before the season",
 guides=["guide-deversement", "guide-entreprise", "guide-souilles"],
 faq_fr=[("Puis-je commander plus de 10 sacs?", "En ligne, une commande compte jusqu'à 10 sacs. Au-delà, demandez une soumission ou écrivez à info@entretienlaval.ca."),
         ("Y a-t-il un prix de volume?", "Oui, le prix distributeur dès 50 sacs : 28 $ couleur et 38 $ blanc le [pack], avant taxes, en ramassage seulement à Laval.")],
 faq_en=[("Can I order more than 10 bags?", "Online, an order holds up to 10 bags. Beyond that, request a quote or email info@entretienlaval.ca."),
         ("Is there a volume price?", "Yes, the distributor price from 50 bags: $28 coloured and $38 white per [pack], before tax, pickup only in Laval.")]))

L.append(dict(key="ville-duvernay", name="Duvernay", zone="laval", img=BAGS,
 fr="/chiffons-guenilles-duvernay/", en="/en/rags-duvernay/", rel=["municipal", "entretien", "guide-papier"],
 title_fr="Chiffons à Duvernay (Laval) : écoles, organismes, immeubles",
 desc_fr="Chiffons recyclés pour écoles, organismes, résidences et immeubles de Duvernay : sac de 25 lb dès 32 $, livraison 15 $ dès 1 sac, facture avec taxes.",
 title_en="Rags in Duvernay, Laval: schools, non-profits, buildings",
 desc_en="Recycled rags for schools, non-profits, residences and buildings in Duvernay, Laval: 25 lb bag from $32, $15 delivery from 1 bag, invoice with tax.",
 intro_fr="Duvernay, dans l'est de Laval, est un quartier de familles, d'écoles et de résidences. Les équipes d'entretien des écoles, des organismes communautaires, des résidences et des copropriétés y utilisent des chiffons toute l'année, souvent avec un budget à respecter.",
 intro_en="Duvernay, in eastern Laval, is a district of families, schools and residences. Maintenance staff in schools, community organizations, residences and condo buildings use rags all year, often on a tight budget.",
 uses_h_fr="Pour les écoles, les organismes et les immeubles", uses_h_en="For schools, non-profits and buildings",
 uses_fr=[("Concierges d'écoles et d'organismes", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> pour l'entretien courant. Voir <a href=\"{{municipal}}\">municipalités et écoles</a>."),
          ("Moins de papier", "un chiffon lavable remplace plusieurs essuie-tout pour l'entretien. Voir <a href=\"{{guide-papier}}\">chiffons recyclés ou essuie-tout</a>."),
          ("Ateliers scolaires", "le <a href=\"{{p-tshirt-blanc}}\">t-shirt blanc</a> pour les ateliers d'arts et de menuiserie.")],
 uses_en=[("School and non-profit custodians", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags for everyday cleaning. See <a href=\"{{municipal}}\">municipalities and schools</a>."),
          ("Less paper", "a washable rag replaces several paper towels for cleaning tasks. See <a href=\"{{guide-papier}}\">recycled rags vs paper towels</a>."),
          ("School shops", "<a href=\"{{p-tshirt-blanc}}\">white T-shirt</a> rags for art and woodworking classes.")],
 ex=[("tshirt-couleur", 3)],
 ex_fr="Un organisme de Duvernay qui prend 3 sacs de t-shirt couleur pour l'entretien de son bâtiment",
 ex_en="A Duvernay non-profit taking 3 bags of coloured T-shirt rags to clean its building",
 guides=["guide-papier", "guide-ranger", "guide-entreprise"],
 faq_fr=[("Recevrons-nous une facture pour notre organisme?", "Oui, une facture d'entreprise enregistrée avec TPS et TVQ (NEQ 2280629637)."),
         ("Les chiffons sont-ils propres pour une école?", "Ils sont lavés à l'eau chaude et traités à la chaleur, sans boutons ni fermetures éclair. Ce sont des chiffons d'entretien, pas des linges pour les aliments.")],
 faq_en=[("Will our organization get an invoice?", "Yes, a registered business invoice with GST and QST (NEQ 2280629637)."),
         ("Are the rags clean enough for a school?", "They are washed in hot water and heat-treated, with no buttons or zippers. They are cleaning rags, not food cloths.")]))

L.append(dict(key="ville-auteuil", name="Auteuil", zone="laval", img=WHITE,
 fr="/chiffons-guenilles-auteuil/", en="/en/rags-auteuil/", rel=["esthetique-auto", "p-tshirt-blanc", "guide-vitres"],
 title_fr="Chiffons à Auteuil (Laval) : esthétique auto et lave-auto",
 desc_fr="Chiffons de coton recyclé pour esthétique automobile, lave-autos et garages d'Auteuil : blanc 42 $, couleur 32 $ le sac de 25 lb, livraison 15 $.",
 title_en="Rags in Auteuil, Laval: car detailing and car washes",
 desc_en="Recycled cotton rags for car detailing, car washes and garages in Auteuil, Laval: white $42, coloured $32 per 25 lb bag, $15 delivery.",
 intro_fr="Auteuil, dans le nord de Laval, compte des ateliers d'esthétique automobile, des lave-autos et des garages de quartier. Leur besoin : beaucoup de chiffons pour les roues, les moteurs et les cadres de portes, et des chiffons propres qui ne marquent pas les vitres.",
 intro_en="Auteuil, in northern Laval, has car detailing shops, car washes and neighbourhood garages. What they need: plenty of rags for wheels, engines and door jambs, and clean rags that don't streak glass.",
 uses_h_fr="Pour l'esthétique auto et les lave-autos", uses_h_en="For car detailing and car washes",
 uses_fr=[("Roues, moteurs, cadres de portes", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> : on salit, on jette, sans user ses microfibres. Voir <a href=\"{{esthetique-auto}}\">esthétique auto et lave-auto</a>."),
          ("Vitres et chromes", "le <a href=\"{{p-tshirt-blanc}}\">t-shirt blanc</a>, peu pelucheux. Voir <a href=\"{{guide-vitres}}\">chiffons pour vitres et inox</a>."),
          ("Peinture de la carrosserie", "gardez vos microfibres pour la peinture; le coton recyclé sert au reste. Voir <a href=\"{{guide-peluches}}\">chiffon non pelucheux</a>.")],
 uses_en=[("Wheels, engines, door jambs", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags: get them dirty and toss them, without wearing out your microfibers. See <a href=\"{{esthetique-auto}}\">car detailing and car wash</a>."),
          ("Glass and chrome", "<a href=\"{{p-tshirt-blanc}}\">white T-shirt</a> rags, low-lint. See <a href=\"{{guide-vitres}}\">rags for glass and stainless steel</a>."),
          ("Paintwork", "keep your microfibers for paint; recycled cotton handles the rest. See <a href=\"{{guide-peluches}}\">lint-free rags</a>.")],
 ex=[("tshirt-couleur", 2), ("tshirt-blanc", 2)],
 ex_fr="Un atelier d'esthétique d'Auteuil qui prend 2 sacs de couleur pour les roues et les moteurs et 2 sacs de blanc pour les vitres",
 ex_en="An Auteuil detailing shop taking 2 coloured bags for wheels and engines and 2 white bags for glass",
 guides=["guide-vitres", "guide-peluches", "guide-garage-mois"],
 faq_fr=[("Les chiffons remplacent-ils la microfibre?", "Pas sur la peinture. Ils remplacent la microfibre pour les roues, les moteurs, les cadres de portes et les gros dégâts, là où elle s'use vite."),
         ("Quel chiffon pour les vitres d'auto?", "Le t-shirt blanc, propre et sec pour la finition. Évitez l'assouplissant si vous les lavez : il laisse des traces.")],
 faq_en=[("Do the rags replace microfiber?", "Not on paint. They replace microfiber for wheels, engines, door jambs and big messes, where it wears out fast."),
         ("Which rag for car windows?", "White T-shirt rags, clean and dry for the final wipe. Skip fabric softener when you wash them: it streaks.")]))

# ---------------- North Shore / South Shore towns ----------------
L.append(dict(key="ville-repentigny", name="Repentigny", zone="rive-nord", img=BAG,
 fr="/chiffons-guenilles-repentigny/", en="/en/rags-repentigny/", rel=["marine", "p-tshirt-couleur", "commander"],
 title_fr="Chiffons et guenilles à Repentigny – livraison 35 $",
 desc_fr="Guenilles recyclées livrées à Repentigny et Le Gardeur : sac de 25 lb, t-shirt couleur 32 $ ou blanc 42 $, livraison 35 $ dès 2 sacs ou ramassage à Laval.",
 title_en="Shop rags in Repentigny – $35 delivery",
 desc_en="Recycled rags delivered in Repentigny and Le Gardeur: 25 lb bag, coloured T-shirt $32 or white $42, $35 delivery from 2 bags, or pickup in Laval.",
 intro_fr="Repentigny, avec son secteur Le Gardeur, est à l'est de Laval, là où la rivière L'Assomption rejoint le fleuve Saint-Laurent. Garages, concessionnaires, entrepreneurs et marinas du bord de l'eau y utilisent des chiffons pour l'huile, la graisse et l'entretien.",
 intro_en="Repentigny, including its Le Gardeur sector, lies east of Laval where the L'Assomption River meets the St. Lawrence. Garages, dealerships, contractors and waterfront marinas there use rags for oil, grease and upkeep.",
 uses_h_fr="Pour les entreprises de Repentigny", uses_h_en="For Repentigny businesses",
 uses_fr=[("Garages et concessionnaires", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> pour l'huile et la graisse. Voir <a href=\"{{garage}}\">chiffons de garage</a>."),
          ("Bateaux et marinas", "couleur pour les moteurs, blanc pour les surfaces visibles. Voir <a href=\"{{marine}}\">marinas et bateaux</a>."),
          ("Entrepreneurs", "un sac par camion pour les outils, la colle et le calfeutrage. Voir <a href=\"{{construction}}\">chantiers</a>.")],
 uses_en=[("Garages and dealerships", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags for oil and grease. See <a href=\"{{garage}}\">garage rags</a>."),
          ("Boats and marinas", "coloured for engines, white for visible surfaces. See <a href=\"{{marine}}\">marinas and boats</a>."),
          ("Contractors", "a bag per truck for tools, glue and caulking. See <a href=\"{{construction}}\">job sites</a>.")],
 ex=[("tshirt-couleur", 2)],
 ex_fr="Un garage de Repentigny qui prend le minimum de 2 sacs de t-shirt couleur",
 ex_en="A Repentigny garage ordering the 2-bag minimum of coloured T-shirt rags",
 guides=["guide-garage-mois", "guide-deversement", "guide-prix"],
 faq_fr=[("Le secteur Le Gardeur est-il livré?", "Oui, Le Gardeur fait partie de Repentigny et de notre zone Rive-Nord, aux mêmes conditions."),
         ("Je n'ai besoin que d'un sac, comment faire?", f"La livraison sur la Rive-Nord commence à 2 sacs. Pour un seul sac, le ramassage est gratuit au {PICKUP}.")],
 faq_en=[("Do you deliver to the Le Gardeur sector?", "Yes, Le Gardeur is part of Repentigny and of our North Shore zone, on the same terms."),
         ("I only need one bag, what can I do?", f"North Shore delivery starts at 2 bags. For a single bag, pickup is free at {PICKUP}.")]))

L.append(dict(key="ville-mascouche", name="Mascouche", zone="rive-nord", img=BALE,
 fr="/chiffons-guenilles-mascouche/", en="/en/rags-mascouche/", rel=["construction", "agriculture", "commander"],
 title_fr="Guenilles à Mascouche : chantiers et transport – livraison 35 $",
 desc_fr="Guenilles recyclées pour chantiers, excavation, transport et fermes à Mascouche : sac de 25 lb à 32 $, livraison 35 $ dès 2 sacs ou ramassage gratuit à Laval.",
 title_en="Shop rags in Mascouche: job sites and trucking – $35 delivery",
 desc_en="Recycled rags for job sites, excavation, trucking and farms in Mascouche: $32 per 25 lb bag, $35 delivery from 2 bags, or free pickup in Laval.",
 intro_fr="Mascouche, voisine de Terrebonne au nord-est de Laval, mêle quartiers en développement et terres agricoles. Entrepreneurs en construction et en excavation, transporteurs et fermes y entretiennent de la machinerie : huile hydraulique, graisse et boue.",
 intro_en="Mascouche, next to Terrebonne northeast of Laval, mixes growing neighbourhoods and farmland. Construction and excavation contractors, carriers and farms maintain machinery there: hydraulic oil, grease and mud.",
 uses_h_fr="Pour les chantiers, le transport et la machinerie", uses_h_en="For job sites, trucking and machinery",
 uses_fr=[("Chantiers", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> pour les outils, le scellant et le ménage de fin de chantier. Voir <a href=\"{{construction}}\">construction et chantiers</a>."),
          ("Camions et machinerie", "graisseurs, huile hydraulique, jauges. Voir <a href=\"{{camions}}\">camions lourds</a> et <a href=\"{{agriculture}}\">machinerie agricole</a>."),
          ("Chiffons souillés au chantier", "un contenant métallique fermé dans la roulotte. Voir <a href=\"{{guide-souilles}}\">chiffons souillés en entreprise</a>.")],
 uses_en=[("Job sites", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags for tools, sealant and end-of-job cleanup. See <a href=\"{{construction}}\">construction and job sites</a>."),
          ("Trucks and machinery", "grease fittings, hydraulic oil, dipsticks. See <a href=\"{{camions}}\">heavy trucks</a> and <a href=\"{{agriculture}}\">farm machinery</a>."),
          ("Dirty rags on site", "a closed metal container in the trailer. See <a href=\"{{guide-souilles}}\">soiled rags at work</a>.")],
 ex=[("tshirt-couleur", 4)],
 ex_fr="Un entrepreneur de Mascouche qui prend 4 sacs de t-shirt couleur pour ses chantiers",
 ex_en="A Mascouche contractor taking 4 bags of coloured T-shirt rags for job sites",
 guides=["guide-souilles", "guide-deversement", "guide-entreprise"],
 faq_fr=[("Pouvez-vous livrer directement au chantier à Mascouche?", "Oui, à l'adresse de votre choix dans la zone Rive-Nord : 35 $ par commande, dès 2 sacs. Indiquez les heures de réception dans les instructions."),
         ("Mascouche a-t-elle une page avec Terrebonne?", "Oui, voir aussi notre page Terrebonne. Mascouche a les mêmes conditions de livraison Rive-Nord.")],
 faq_en=[("Can you deliver straight to a Mascouche job site?", "Yes, to any address in the North Shore zone: $35 per order, from 2 bags. Add receiving hours in the instructions."),
         ("Is Mascouche covered with Terrebonne?", "Yes, see our Terrebonne page too. Mascouche has the same North Shore delivery terms.")]))

L.append(dict(key="ville-saint-eustache", name="Saint-Eustache", zone="rive-nord", img=SHOP,
 fr="/chiffons-guenilles-saint-eustache/", en="/en/rags-saint-eustache/", rel=["usinage", "soudure", "guide-solvants"],
 title_fr="Chiffons d'atelier à Saint-Eustache – livraison 35 $",
 desc_fr="Chiffons d'atelier recyclés pour usinage, fabrication et garages à Saint-Eustache : sac de 25 lb dès 32 $, livraison 35 $ dès 2 sacs, ou ramassage à Laval.",
 title_en="Shop rags in Saint-Eustache – $35 delivery",
 desc_en="Recycled shop rags for machining, fabrication and garages in Saint-Eustache: 25 lb bag from $32, $35 delivery from 2 bags, or pickup in Laval.",
 intro_fr="Saint-Eustache, juste à l'ouest de Laval de l'autre côté de la rivière des Mille Îles, a ses parcs industriels, ses ateliers de fabrication et ses garages. Dans un atelier, les chiffons servent à l'huile de coupe, aux solvants de nettoyage et à l'entretien des machines.",
 intro_en="Saint-Eustache, just west of Laval across the Rivière des Mille Îles, has industrial parks, fabrication shops and garages. In a shop, rags handle cutting oil, cleaning solvents and machine upkeep.",
 uses_h_fr="Pour les ateliers et les usines", uses_h_en="For shops and plants",
 uses_fr=[("Usinage", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> pour l'huile de coupe et les machines, le <a href=\"{{p-tshirt-blanc}}\">blanc</a> pour les pièces finies. Voir <a href=\"{{usinage}}\">usinage et ateliers</a>."),
          ("Soudure et fabrication", "du blanc pour dégraisser avant la soudure ou la peinture. Voir <a href=\"{{soudure}}\">soudure et fabrication métallique</a>."),
          ("Solvants", "acétone, diluant, alcool : le coton résiste, le blanc ne déteint pas. Voir <a href=\"{{guide-solvants}}\">chiffons et solvants</a>.")],
 uses_en=[("Machining", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags for cutting oil and machines, <a href=\"{{p-tshirt-blanc}}\">white</a> for finished parts. See <a href=\"{{usinage}}\">machine shops</a>."),
          ("Welding and fabrication", "white rags to degrease before welding or painting. See <a href=\"{{soudure}}\">welding and metal fabrication</a>."),
          ("Solvents", "acetone, thinner, alcohol: cotton holds up, white doesn't bleed. See <a href=\"{{guide-solvants}}\">rags and solvents</a>.")],
 ex=[("tshirt-couleur", 3), ("tshirt-blanc", 1)],
 ex_fr="Un atelier d'usinage de Saint-Eustache qui prend 3 sacs de couleur pour les machines et 1 sac de blanc pour l'inspection des pièces",
 ex_en="A Saint-Eustache machine shop taking 3 coloured bags for machines and 1 white bag for part inspection",
 guides=["guide-solvants", "guide-metal", "guide-souilles"],
 faq_fr=[("Livrez-vous aussi Deux-Montagnes?", "Oui, Deux-Montagnes fait aussi partie de notre zone Rive-Nord : 35 $ par commande, dès 2 sacs."),
         ("Quel chiffon pour l'huile de coupe sur des pièces finies?", "Le t-shirt blanc, sans transfert de teinture. La ratine est en rupture de stock pour le moment.")],
 faq_en=[("Do you deliver to Deux-Montagnes too?", "Yes, Deux-Montagnes is also in our North Shore zone: $35 per order, from 2 bags."),
         ("Which rag for cutting oil on finished parts?", "White T-shirt rags, with no dye transfer. Terry is out of stock for now.")]))

L.append(dict(key="ville-rosemere", name="Rosemère", zone="rive-nord", img=BAGS,
 fr="/chiffons-guenilles-rosemere/", en="/en/rags-rosemere/", rel=["restauration", "entretien", "commander"],
 title_fr="Chiffons à Rosemère : commerces et restaurants – livraison 35 $",
 desc_fr="Chiffons recyclés pour restaurants, commerces et entretien ménager à Rosemère : sac de 25 lb, couleur 32 $ ou blanc 42 $, livraison 35 $ dès 2 sacs.",
 title_en="Rags in Rosemère: shops and restaurants – $35 delivery",
 desc_en="Recycled rags for restaurants, shops and cleaning companies in Rosemère: 25 lb bag, coloured $32 or white $42, $35 delivery from 2 bags.",
 intro_fr="Rosemère, juste au nord de Laval de l'autre côté de la rivière des Mille Îles, est connue pour son secteur commercial autour de Place Rosemère. Restaurants, commerces et entreprises d'entretien ménager y ont besoin de chiffons pour la graisse, l'inox, les vitres et les planchers.",
 intro_en="Rosemère, just north of Laval across the Rivière des Mille Îles, is known for its retail area around Place Rosemère. Restaurants, shops and cleaning companies there need rags for grease, stainless steel, glass and floors.",
 uses_h_fr="Pour les restaurants, les commerces et l'entretien", uses_h_en="For restaurants, shops and cleaning",
 uses_fr=[("Cuisines", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> pour la graisse des hottes et les planchers. Voir <a href=\"{{restauration}}\">restaurants et cuisines</a>."),
          ("Inox et vitrines", "le <a href=\"{{p-tshirt-blanc}}\">t-shirt blanc</a>. Voir <a href=\"{{guide-vitres}}\">chiffons pour vitres et inox</a>."),
          ("Entreprises d'entretien", "livraisons régulières au même prix. Voir <a href=\"{{entretien}}\">entretien ménager</a>.")],
 uses_en=[("Kitchens", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags for hood grease and floors. See <a href=\"{{restauration}}\">restaurants and kitchens</a>."),
          ("Stainless and shop windows", "<a href=\"{{p-tshirt-blanc}}\">white T-shirt</a> rags. See <a href=\"{{guide-vitres}}\">rags for glass and stainless steel</a>."),
          ("Cleaning companies", "regular deliveries at the same price. See <a href=\"{{entretien}}\">janitorial rags</a>.")],
 ex=[("tshirt-couleur", 1), ("tshirt-blanc", 1)],
 ex_fr="Un restaurant de Rosemère qui prend 1 sac de couleur pour la cuisine et 1 sac de blanc pour l'inox (2 sacs, le minimum Rive-Nord)",
 ex_en="A Rosemère restaurant taking 1 coloured bag for the kitchen and 1 white bag for stainless steel (2 bags, the North Shore minimum)",
 guides=["guide-vitres", "guide-papier", "guide-huileux"],
 faq_fr=[("Peut-on utiliser ces chiffons sur les comptoirs de cuisine?", "Pour les surfaces en contact avec les aliments, utilisez des linges réservés à cet usage selon les règles du MAPAQ. Nos chiffons servent à l'entretien : graisse, planchers, équipement, inox."),
         ("Puis-je mélanger couleur et blanc pour atteindre 2 sacs?", "Oui, le minimum de 2 sacs s'applique au total de la commande.")],
 faq_en=[("Can these rags be used on kitchen counters?", "For food-contact surfaces, use dedicated cloths under MAPAQ rules. Our rags are for cleaning: grease, floors, equipment, stainless steel."),
         ("Can I mix coloured and white to reach 2 bags?", "Yes, the 2-bag minimum applies to the order total.")]))

L.append(dict(key="ville-brossard", name="Brossard", zone="rive-sud", img=BAG,
 fr="/chiffons-guenilles-brossard/", en="/en/rags-brossard/", rel=["restauration", "carrosserie", "commander"],
 title_fr="Chiffons et guenilles à Brossard – livraison 35 $",
 desc_fr="Chiffons recyclés livrés à Brossard : restaurants du DIX30, garages, entretien ménager. Sac de 25 lb dès 32 $, livraison 35 $ dès 2 sacs ou ramassage à Laval.",
 title_en="Rags and shop rags in Brossard – $35 delivery",
 desc_en="Recycled rags delivered in Brossard: DIX30 restaurants, garages, cleaning crews. 25 lb bag from $32, $35 delivery from 2 bags, or pickup in Laval.",
 intro_fr="Brossard, sur la Rive-Sud face à Montréal, réunit un grand pôle commercial avec le Quartier DIX30, des bureaux et, le long du boulevard Taschereau, beaucoup de garages et de concessionnaires. Restaurants, équipes d'entretien et ateliers y utilisent des chiffons tous les jours.",
 intro_en="Brossard, on the South Shore facing Montréal, has a large retail hub with Quartier DIX30, offices and, along Taschereau Boulevard, many garages and dealerships. Restaurants, cleaning crews and shops there use rags every day.",
 uses_h_fr="Pour les entreprises de Brossard", uses_h_en="For Brossard businesses",
 uses_fr=[("Restaurants et commerces", "couleur pour la graisse, blanc pour l'inox. Voir <a href=\"{{restauration}}\">restaurants et cuisines</a>."),
          ("Garages et concessionnaires", "le <a href=\"{{p-tshirt-couleur}}\">t-shirt couleur</a> pour la mécanique, le <a href=\"{{p-tshirt-blanc}}\">blanc</a> pour la préparation esthétique. Voir <a href=\"{{garage}}\">chiffons de garage</a>."),
          ("Entretien de bureaux", "chiffons lavables à la place d'une partie du papier. Voir <a href=\"{{entretien}}\">entretien ménager</a>.")],
 uses_en=[("Restaurants and shops", "coloured for grease, white for stainless steel. See <a href=\"{{restauration}}\">restaurants and kitchens</a>."),
          ("Garages and dealerships", "<a href=\"{{p-tshirt-couleur}}\">coloured T-shirt</a> rags for mechanics, <a href=\"{{p-tshirt-blanc}}\">white</a> for detailing prep. See <a href=\"{{garage}}\">garage rags</a>."),
          ("Office cleaning", "washable rags instead of some of the paper. See <a href=\"{{entretien}}\">janitorial rags</a>.")],
 ex=[("tshirt-couleur", 2), ("tshirt-blanc", 2)],
 ex_fr="Un concessionnaire de Brossard qui prend 2 sacs de couleur pour l'atelier et 2 sacs de blanc pour la préparation des véhicules",
 ex_en="A Brossard dealership taking 2 coloured bags for the shop and 2 white bags for vehicle prep",
 guides=["guide-vitres", "guide-garage-mois", "guide-entreprise"],
 faq_fr=[("Brossard fait-elle partie de la zone Rive-Sud?", "Oui : livraison 35 $ par commande, dès 2 sacs, en 1 à 3 jours ouvrables après le paiement. Le formulaire vérifie votre code postal."),
         ("Livrez-vous aussi Longueuil et Saint-Lambert?", "Oui, aux mêmes conditions Rive-Sud. Voir aussi notre page Longueuil.")],
 faq_en=[("Is Brossard in the South Shore zone?", "Yes: $35 delivery per order, from 2 bags, within 1 to 3 business days of payment. The form checks your postal code."),
         ("Do you also deliver to Longueuil and Saint-Lambert?", "Yes, on the same South Shore terms. See our Longueuil page too.")]))


def _money(n, lang):
    return f"{n} $" if lang == "fr" else f"${n:,}"


def _example(d, lang):
    z = ZONES[d["zone"]]
    goods = sum(PRICE[p] * q for p, q in d["ex"])
    parts = " + ".join(f"{q} × {_money(PRICE[p], lang)}" for p, q in d["ex"])
    tot = goods + z["fee"]
    if lang == "fr":
        return (f"<p>{d['ex_fr']} paie {parts} + {_money(z['fee'], lang)} de livraison = <b>{_money(tot, lang)} avant taxes</b>. "
                f"En ramassage gratuit à Laval : {_money(goods, lang)} avant taxes. Exemple de calcul seulement; TPS et TVQ en sus.</p>")
    return (f"<p>{d['ex_en']} pays {parts} + {_money(z['fee'], lang)} delivery = <b>{_money(tot, lang)} before tax</b>. "
            f"With free pickup in Laval: {_money(goods, lang)} before tax. Example calculation only; GST and QST extra.</p>")


def _zone_text(d, lang):
    z = ZONES[d["zone"]]; n = d["name"]; zn = ZONE_NAME[d["zone"]][0 if lang == "fr" else 1]
    if lang == "fr":
        mn = "dès 1 sac" if z["min_bags"] <= 1 else f"minimum {z['min_bags']} sacs"
        extra = " (codes postaux H7)" if d["zone"] == "laval" else ""
        return (f"<p><b>Livraison à {n} : {z['fee']} $ par commande, {mn}</b>, en {DAYS['fr']} après le paiement. "
                f"{n} fait partie de notre zone {zn}{extra} : vous pouvez <a href=\"{{{{commander}}}}\">commander en ligne</a> et payer par PayPal ou carte.</p>")
    mn = "from 1 bag" if z["min_bags"] <= 1 else f"minimum {z['min_bags']} bags"
    extra = " (H7 postal codes)" if d["zone"] == "laval" else ""
    return (f"<p><b>Delivery in {n}: ${z['fee']} per order, {mn}</b>, within {DAYS['en']} of payment. "
            f"{n} is in our {zn} zone{extra}: you can <a href=\"{{{{commander}}}}\">order online</a> and pay with PayPal or card.</p>")


def _stock(lang):
    gone = [p for p in ("ratine-couleur", "ratine-blanc") if p in O.CHECKOUT["unavailable"]]
    if not gone:
        return ""
    return ("<li>Ratine couleur et blanche : en rupture de stock pour le moment.</li>" if lang == "fr"
            else "<li>Coloured and white terry: out of stock for now.</li>")


def _body(d, lang, titles):
    fr = lang == "fr"; n = d["name"]
    uses = "".join(f"<li><b>{a}</b> : {b}</li>" if fr else f"<li><b>{a}</b>: {b}</li>" for a, b in d["uses_" + lang])
    guides = " · ".join(f'<a href="{{{{{g}}}}}">{titles[g][lang]}</a>' for g in d["guides"])
    laval = d["zone"] == "laval"
    if fr:
        pick = (f"<p>Le ramassage est gratuit dès 1 sac au {PICKUP}. Commandez en ligne en choisissant « Ramassage » : nous vous écrivons quand la commande est prête."
                + (" Depuis un quartier de Laval, c'est souvent le plus simple pour un seul sac." if laval else f" C'est la solution si vous n'avez besoin que d'un sac : la livraison à {n} commence à {ZONES[d['zone']]['min_bags']} sacs.") + "</p>")
        return f"""<h2>Livraison à {n}</h2>
<p>{d['intro_fr']}</p>
{_zone_text(d, 'fr')}
<h2>{d['uses_h_fr']}</h2>
<ul>{uses}</ul>
<h2>Exemple de commande</h2>
{_example(d, 'fr')}
<h2>Ramassage gratuit à Laval</h2>
{pick}
<h2>Nos chiffons et nos prix</h2>
<ul><li><a href="{{{{p-tshirt-couleur}}}}">T-shirt couleur</a> : 32 $ le [pack] (11,3 kg), avant taxes.</li>
<li><a href="{{{{p-tshirt-blanc}}}}">T-shirt blanc</a> : 42 $ le [pack], sans transfert de couleur.</li>{_stock('fr')}</ul>
<p>Chiffons de coton recyclé lavés à l'eau chaude, triés et traités à la chaleur, sans boutons ni fermetures éclair. Distributeurs, dès 50 sacs : 28 $ couleur et 38 $ blanc, en ramassage seulement (voir <a href="{{{{gros}}}}">guenilles en gros</a>).</p>
<h2>Guides utiles</h2>
<p>{guides}</p>
<h2>Commander</h2>
<p><a href="{{{{commander}}}}">Commandez en ligne</a> (jusqu'à 10 sacs), demandez une <a href="{{{{home#devis}}}}">soumission</a>, appelez le 438-831-3611 ou écrivez à info@entretienlaval.ca.</p>"""
    pick = (f"<p>Pickup is free from 1 bag at {PICKUP}. Order online and choose “Pickup”: we email you when the order is ready."
            + (" From a Laval neighbourhood, it's often the simplest option for a single bag." if laval else f" It's the way to go if you only need one bag: delivery in {n} starts at {ZONES[d['zone']]['min_bags']} bags.") + "</p>")
    return f"""<h2>Delivery in {n}</h2>
<p>{d['intro_en']}</p>
{_zone_text(d, 'en')}
<h2>{d['uses_h_en']}</h2>
<ul>{uses}</ul>
<h2>Example order</h2>
{_example(d, 'en')}
<h2>Free pickup in Laval</h2>
{pick}
<h2>Our rags and prices</h2>
<ul><li><a href="{{{{p-tshirt-couleur}}}}">Coloured T-shirt</a>: $32 per [pack] (11.3 kg), before tax.</li>
<li><a href="{{{{p-tshirt-blanc}}}}">White T-shirt</a>: $42 per [pack], no colour transfer.</li>{_stock('en')}</ul>
<p>Recycled cotton rags washed in hot water, sorted and heat-treated, with no buttons or zippers. Distributors, from 50 bags: $28 coloured and $38 white, pickup only (see <a href="{{{{gros}}}}">wholesale rags</a>).</p>
<h2>Useful guides</h2>
<p>{guides}</p>
<h2>How to order</h2>
<p><a href="{{{{commander}}}}">Order online</a> (up to 10 bags), request a <a href="{{{{home#devis}}}}">quote</a>, call 438-831-3611 or email info@entretienlaval.ca.</p>"""


def _faq(d, lang):
    z = ZONES[d["zone"]]; n = d["name"]
    if lang == "fr":
        mn = "dès 1 sac" if z["min_bags"] <= 1 else f"minimum {z['min_bags']} sacs"
        base = [(f"Combien coûte la livraison à {n}?", f"{z['fee']} $ par commande, {mn}, avant taxes. Livraison en {DAYS['fr']} après le paiement, ou ramassage gratuit au {PICKUP}.")]
    else:
        mn = "from 1 bag" if z["min_bags"] <= 1 else f"minimum {z['min_bags']} bags"
        base = [(f"How much is delivery in {n}?", f"${z['fee']} per order, {mn}, before tax. Delivered within {DAYS['en']} of payment, or free pickup at {PICKUP}.")]
    return base + d["faq_" + lang]


def _page(d, titles):
    n = d["name"]; zf = ZONES[d["zone"]]["fee"]
    return {"kind": "city", "img": d["img"], "rel": d["rel"], "city": n, "city_en": n, "core": d["zone"] == "laval",
     "fr": {"path": d["fr"], "short": n, "title": d["title_fr"], "desc": d["desc_fr"],
            "eyebrow": "Livraison · " + n, "h1": f"Guenilles et chiffons d'essuyage à {n}",
            "lede": f"Chiffons de coton recyclé en [packs], lavés à l'eau chaude et traités à la chaleur, livrés à {n} pour {zf} $ ou à ramasser gratuitement à Laval.",
            "card": f"Livraison {zf} $" + (", dès 1 sac." if ZONES[d["zone"]]["min_bags"] <= 1 else f", dès {ZONES[d['zone']]['min_bags']} sacs."),
            "alt": f"Sac de chiffons recyclés de 25 lb livré à {n}", "body": _body(d, "fr", titles), "faq": _faq(d, "fr")},
     "en": {"path": d["en"], "short": n, "title": d["title_en"], "desc": d["desc_en"],
            "eyebrow": "Delivery · " + n, "h1": f"Rags and shop rags in {n}",
            "lede": f"Recycled cotton rags in [packs], washed in hot water and heat-treated, delivered in {n} for ${zf} or free to pick up in Laval.",
            "card": f"${zf} delivery" + (", from 1 bag." if ZONES[d["zone"]]["min_bags"] <= 1 else f", from {ZONES[d['zone']]['min_bags']} bags."),
            "alt": f"25 lb bag of recycled rags delivered in {n}", "body": _body(d, "en", titles), "faq": _faq(d, "en")}}


def pages(all_pages):
    """Build the local pages. Guide link text comes from the guides' own short titles."""
    titles = {k: {l: p[l]["short"] for l in ("fr", "en")} for k, p in all_pages.items()}
    return {d["key"]: _page(d, titles) for d in L}


LAVAL_KEYS = [d["key"] for d in L if d["zone"] == "laval"]
SHORE_KEYS = [d["key"] for d in L if d["zone"] != "laval"]
LOCAL_KEYS = LAVAL_KEYS + SHORE_KEYS
