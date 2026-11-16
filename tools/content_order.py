"""Online ordering (PayPal) for Laval, Montréal, Rive-Sud, Rive-Nord + free pickup: settings and page text.

LEGAL NOTE: no PayPal/card fee is added to the customer's bill.
- PayPal's user agreement ("No surcharges") forbids charging a fee for paying with PayPal.
- Québec's Consumer Protection Act forbids card surcharges to consumers.
GST and QST are added (required). The delivery fee is the same whatever the payment method.
"""

CHECKOUT = {
    # ---- Owner sets these ----
    # Delivery zones, matched by postal-code prefix (first match wins). Fee in CAD before tax.
    "zones": [
        {"id": "laval", "name": "Laval", "prefixes": ["H7"], "fee": 15, "min_bags": 1,
         "fr": "code postal H7", "en": "postal code H7"},
        {"id": "montreal", "name": "Montréal", "prefixes": ["H"], "fee": 25, "min_bags": 2,
         "fr": "autres codes postaux en H", "en": "other H postal codes"},
        {"id": "rive-sud", "name": "Rive-Sud", "prefixes": ["J4", "J3Y", "J3V", "J5R", "J6J", "J6K"], "fee": 35, "min_bags": 2,
         "fr": "Longueuil, Brossard, Boucherville, Saint-Lambert, Saint-Hubert, Saint-Bruno, La Prairie, Châteauguay",
         "en": "Longueuil, Brossard, Boucherville, Saint-Lambert, Saint-Hubert, Saint-Bruno, La Prairie, Châteauguay"},
        {"id": "rive-nord", "name": "Rive-Nord", "prefixes": ["J6W", "J6X", "J6Y", "J7M", "J7K", "J7L", "J5Y", "J5Z", "J6A", "J6Z",
                                                            "J7A", "J7B", "J7C", "J7E", "J7G", "J7H", "J7P", "J7R", "J7J"], "fee": 35, "min_bags": 2,
         "fr": "Terrebonne, Mascouche, Repentigny, Bois-des-Filion, Lorraine, Rosemère, Blainville, Sainte-Thérèse, Boisbriand, Saint-Eustache, Deux-Montagnes, Mirabel",
         "en": "Terrebonne, Mascouche, Repentigny, Bois-des-Filion, Lorraine, Rosemère, Blainville, Sainte-Thérèse, Boisbriand, Saint-Eustache, Deux-Montagnes, Mirabel"},
    ],
    # Free pickup at the shop, no address needed, from 1 bag.
    "pickup": {"id": "pickup", "name": "Ramassage à Laval", "fee": 0, "min_bags": 1, "address": "1355 boul. Le Corbusier, Laval"},
    # Product ids not sold online right now (shown as out of stock, refused by the server).
    "unavailable": ["ratine-couleur", "ratine-blanc"],
    "free_delivery_from": None,  # number of bags from which delivery is free, or None for never
    "max_bags": 10,              # most bags per online order; bigger orders go through the quote form
    "paypal_client_id": "BAA7CVLL36x2u_-E5rZ-Hd6kbJU89nTnWcq-4QA6O_QuCEfR20y8CqcHqKdD50_H2ElEgc0tfhci7wy2wQ",      # PUBLIC Client ID from developer.paypal.com (sandbox one while testing). The SECRET never goes here.
    # ---- fixed ----
    "gst": 0.05,                 # TPS
    "qst": 0.09975,              # TVQ
    "postal_regex": r"^[HJ]\d[A-Z] ?\d[A-Z]\d$",  # H = Montréal island + Laval, J = the zones' FSAs above
}

def ready():
    return bool(CHECKOUT["zones"]) and bool(CHECKOUT["paypal_client_id"])

PAGE = {"kind": "order", "img": None, "rel": ["couleur", "blancs", "gros"],
 "fr": {"path": "/commander/", "short": "Commander en ligne",
  "title": "Guenilles en ligne – Laval, Montréal, Rives | Chiffons ÉCO",
  "desc": "Commandez vos guenilles en ligne : sacs de 25 lb dès 32 $, livrés à Laval, Montréal, Rive-Sud et Rive-Nord, ou ramassage gratuit à Laval.",
  "eyebrow": "Commande en ligne · Laval, Montréal, Rive-Sud, Rive-Nord", "h1": "Commander des chiffons en ligne",
  "lede": "Choisissez vos sacs, la livraison ou le ramassage gratuit à Laval, et payez par PayPal ou carte de crédit. Livraison en [days] après le paiement. Pour les autres régions ou les grosses commandes, demandez une soumission.",
  "card": "Payez en ligne par PayPal ou carte, livré à Laval, Montréal, Rive-Sud et Rive-Nord.",
  "body": """<h2>Comment ça fonctionne</h2>
<ol><li>Choisissez les produits et le nombre de [packs].</li><li>Choisissez la livraison à votre adresse (Laval, Montréal, Rive-Sud ou Rive-Nord) ou le ramassage gratuit à Laval, et entrez vos coordonnées.</li><li>Payez par PayPal ou par carte de crédit ou débit, sans compte PayPal.</li><li>Livraison en [days] après le paiement : nous vous contactons pour fixer l'heure. Pour un ramassage, nous vous écrivons quand la commande est prête.</li></ol>
<h2>Livraison et ramassage</h2>
<p>[delivery]</p>
<h2>Disponibilité</h2>
<p>[stock]</p>
<h2>Prix et taxes</h2>
<p>Les prix sont affichés avant taxes. La TPS (5 %) et la TVQ (9,975 %) sont calculées sur les produits et la livraison, et affichées avant le paiement. Le prix est le même quel que soit le mode de paiement. Vous recevez une facture d'entreprise enregistrée.</p>
<h2>Retours</h2>
<p>Toutes les ventes sont finales : nous n'acceptons pas les retours. Si vous recevez un mauvais produit ou un [pack] endommagé, écrivez à info@entretienlaval.ca et nous le remplaçons.</p>
<h2>Autres régions, grosses commandes, virement Interac</h2>
<p>Hors de ces secteurs, pour plus de [max] [packs], ou pour payer par virement Interac, <a href="{{home#devis}}">demandez une soumission</a> ou écrivez à info@entretienlaval.ca.</p>""",
  "faq": [("Dois-je avoir un compte PayPal?", "Non. Le bouton carte permet de payer par carte de crédit ou de débit sans compte PayPal."),
          ("Quand suis-je livré?", "En [days] après le paiement. Nous vous contactons pour fixer l'heure de livraison."),
          ("Puis-je ramasser ma commande?", "Oui, gratuitement, dès 1 sac, au [pickup]. Choisissez « Ramassage » dans le formulaire : nous vous écrivons quand la commande est prête."),
          ("Combien coûte la livraison?", "[delivery]"),
          ("Y a-t-il des frais pour payer en ligne?", "Non. Vous payez le prix des produits, la livraison et les taxes, comme pour une commande par soumission."),
          ("Puis-je retourner ma commande?", "Non, toutes les ventes sont finales. Si vous recevez un mauvais produit ou un [pack] endommagé, écrivez à info@entretienlaval.ca et nous le remplaçons.")]},
 "en": {"path": "/en/order/", "short": "Order online",
  "title": "Order rags online – Laval, Montréal, Shores | ECO Rags",
  "desc": "Order recycled rags online: 25 lb bags from $32, delivered in Laval, Montréal and both Shores, or free pickup in Laval. PayPal or card.",
  "eyebrow": "Online order · Laval, Montréal, South Shore, North Shore", "h1": "Order rags online",
  "lede": "Pick your bags, delivery or free pickup in Laval, and pay with PayPal or a credit card. Delivered within [days] of payment. For other regions or large orders, request a quote.",
  "card": "Pay online with PayPal or card, delivered in Laval, Montréal and both Shores.",
  "body": """<h2>How it works</h2>
<ol><li>Choose the products and the number of [packs].</li><li>Choose delivery to your address (Laval, Montréal, South Shore or North Shore) or free pickup in Laval, and enter your contact details.</li><li>Pay with PayPal, or with a credit or debit card without a PayPal account.</li><li>Delivered within [days] of payment: we contact you to set the time. For pickup, we email you when the order is ready.</li></ol>
<h2>Delivery and pickup</h2>
<p>[delivery]</p>
<h2>Availability</h2>
<p>[stock]</p>
<h2>Prices and taxes</h2>
<p>Prices are shown before tax. GST (5%) and QST (9.975%) are calculated on the products and delivery and shown before you pay. The price is the same whatever the payment method. You get a registered business invoice.</p>
<h2>Returns</h2>
<p>All sales are final: we do not accept returns. If you receive the wrong product or a damaged [pack], email info@entretienlaval.ca and we will replace it.</p>
<h2>Other regions, large orders, Interac e-Transfer</h2>
<p>Outside these areas, for more than [max] [packs], or to pay by Interac e-Transfer, <a href="{{home#devis}}">request a quote</a> or email info@entretienlaval.ca.</p>""",
  "faq": [("Do I need a PayPal account?", "No. The card button lets you pay with a credit or debit card without a PayPal account."),
          ("When is it delivered?", "Within [days] of payment. We contact you to set the delivery time."),
          ("Can I pick up my order?", "Yes, free, from 1 bag, at [pickup]. Choose “Pickup” in the form: we email you when the order is ready."),
          ("How much is delivery?", "[delivery]"),
          ("Is there a fee for paying online?", "No. You pay the product price, delivery and taxes, the same as an order by quote."),
          ("Can I return my order?", "No, all sales are final. If you receive the wrong product or a damaged [pack], email info@entretienlaval.ca and we will replace it.")]}}

DAYS = {"fr": "1 à 3 jours ouvrables", "en": "1 to 3 business days"}

def _delivery(lang):
    out = []
    for z in CHECKOUT["zones"]:
        fee = f"{z['fee']} $" if lang == "fr" else f"${z['fee']}"
        if lang == "fr":
            mn = "dès 1 sac" if z["min_bags"] <= 1 else f"minimum {z['min_bags']} sacs"
            out.append(f"{z['name']} ({z['fr']}) : {fee} par commande, {mn}")
        else:
            mn = "from 1 bag" if z["min_bags"] <= 1 else f"minimum {z['min_bags']} bags"
            out.append(f"{z['name']} ({z['en']}): {fee} per order, {mn}")
    pk = CHECKOUT["pickup"]["address"]
    out.append(f"Ramassage au {pk} : gratuit, dès 1 sac" if lang == "fr" else f"Pickup at {pk}: free, from 1 bag")
    return ". ".join(out) + (". Taxes en sus." if lang == "fr" else ". Plus tax.")

def _stock(lang):
    ids = set(CHECKOUT["unavailable"])
    from content import PRODUCTS
    gone = [p[lang][0] for p in PRODUCTS if p["id"] in ids]
    have = [p[lang][0] for p in PRODUCTS if p["id"] not in ids]
    if not gone:
        return "Tous les produits sont en stock." if lang == "fr" else "All products are in stock."
    if lang == "fr":
        return f"En rupture de stock pour le moment : {', '.join(gone)}. Disponibles : {', '.join(have)}."
    return f"Out of stock for now: {', '.join(gone)}. Available: {', '.join(have)}."

def _fill(t, lang):
    return (t.replace("[max]", str(CHECKOUT["max_bags"])).replace("[delivery]", _delivery(lang)).replace("[days]", DAYS[lang])
             .replace("[stock]", _stock(lang)).replace("[pickup]", CHECKOUT["pickup"]["address"]))

for _l in ("fr", "en"):
    for _k in ("body", "lede", "desc"):
        PAGE[_l][_k] = _fill(PAGE[_l][_k], _l)
    PAGE[_l]["faq"] = [(q, _fill(a, _l)) for q, a in PAGE[_l]["faq"]]

UI = {
 "fr": {"qty": "Nombre de sacs", "contact_h": "Vos coordonnées et l'adresse de livraison", "mail_note": "Si votre commande n'est pas terminée, nous pourrions vous écrire une seule fois pour savoir ce qui a bloqué.", "mode_h": "Livraison ou ramassage", "m_del": "Livraison à mon adresse", "m_pick": "Ramassage gratuit à Laval", "pickup": "Ramassage", "oos": "rupture de stock", "name": "Nom", "company": "Entreprise", "email": "Courriel",
        "phone": "Téléphone", "address": "Adresse (numéro, rue, local)", "city": "Ville", "postal": "Code postal", "notes": "Instructions de livraison",
        "sum_h": "Votre commande", "goods": "Produits", "delivery": "Livraison", "free": "Gratuite", "gst": "TPS (5 %)", "qst": "TVQ (9,975 %)", "total": "Total",
        "e_bags": "Choisissez entre 1 et {max} sacs.", "e_fields": "Remplissez les champs obligatoires.", "e_min": "Minimum {min} sacs pour une livraison à {zone}.", "e_stock": "Ce produit est en rupture de stock pour le moment.", "e_postal": "La livraison en ligne est offerte à Laval, Montréal, sur la Rive-Sud et la Rive-Nord (voir les villes plus bas). Vérifiez le code postal, choisissez le ramassage gratuit à Laval ou demandez une soumission.",
        "e_pay": "Le paiement n'a pas pu être complété. Aucun montant n'a été prélevé. Réessayez ou appelez le 438-831-3611.",
        "e_after": "Paiement reçu, mais la confirmation n'a pas pu être envoyée. Notez ce numéro et appelez le 438-831-3611 : ",
        "note": "Prix avant taxes. TPS et TVQ ajoutées. Aucuns frais selon le mode de paiement.", "pay_h": "Paiement"},
 "en": {"qty": "Number of bags", "contact_h": "Your details and delivery address", "mail_note": "If your order is not completed, we may email you once to ask what went wrong.", "mode_h": "Delivery or pickup", "m_del": "Delivery to my address", "m_pick": "Free pickup in Laval", "pickup": "Pickup", "oos": "out of stock", "name": "Name", "company": "Company", "email": "Email",
        "phone": "Phone", "address": "Address (number, street, unit)", "city": "City", "postal": "Postal code", "notes": "Delivery instructions",
        "sum_h": "Your order", "goods": "Products", "delivery": "Delivery", "free": "Free", "gst": "GST (5%)", "qst": "QST (9.975%)", "total": "Total",
        "e_bags": "Choose between 1 and {max} bags.", "e_fields": "Please fill in the required fields.", "e_min": "Minimum {min} bags for delivery in {zone}.", "e_stock": "This product is out of stock for now.", "e_postal": "Online delivery is for Laval, Montréal, the South Shore and the North Shore (see the towns below). Check the postal code, choose free pickup in Laval or request a quote.",
        "e_pay": "The payment could not be completed. Nothing was charged. Try again or call 438-831-3611.",
        "e_after": "Payment received, but the confirmation could not be sent. Note this number and call 438-831-3611: ",
        "note": "Prices before tax. GST and QST added. No fee based on payment method.", "pay_h": "Payment"},
}
