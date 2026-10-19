# French–English Glossary — Gestion Informatisée

Use the French terms for ILEIC lessons and the English explanations when studying the software design.

| French term | English meaning | Plain explanation |
|---|---|---|
| Gestion informatisée | Computerised management | Using software to organise management information. |
| Système d'information | Information system | People, procedures, information and tools used to manage work. |
| Système modulaire | Modular system | A system made of separate feature groups that can be added as needed. |
| Organisation pilote | Pilot organisation | The first example used to study and test the system. |
| Cadrage du projet | Project framing | Agreeing on purpose, limits and direction. |
| Analyse du besoin | Requirements/needs analysis | Understanding the user's problem before deciding what to build. |
| Processus métier | Business process | The steps people follow to complete a business activity. |
| Exigence fonctionnelle | Functional requirement | Something the software must allow or do. |
| Règle de gestion | Business rule | A policy or condition the process/software must respect. |
| Donnée | Data | A recorded fact, such as a product code or quantity. |
| Enregistrement | Record | A saved set of information about something. |
| Base de données | Database | An organised collection of related information. |
| Modélisation des données | Data modelling | Deciding which records exist and how they relate. |
| Entité | Entity | A kind of thing the software stores information about. |
| Champ | Field | One attribute in a record. |
| Référence produit | Product reference/SKU | An identifier that distinguishes a stock-controlled variant. |
| Stock | Stock/inventory | Goods held by the organisation. |
| Gestion des stocks | Inventory management | Tracking quantities and changes in stock. |
| Mouvement de stock | Stock movement | A traceable event that changes usable stock. |
| Entrée en stock | Stock entry | Goods added to stock. |
| Sortie de stock | Stock exit | Goods removed from stock. |
| Stock initial | Starting stock | Quantity before a calculation/period. |
| Stock final | Ending stock | Quantity after entries and exits. |
| Commande fournisseur / bon de commande (BC) | Purchase order | What the shop requests from a supplier; not proof goods arrived. |
| Approvisionnement | Procurement/replenishment | Getting goods the organisation needs. |
| Réception des marchandises | Goods receipt | Physically receiving and checking a delivery. |
| Bon de livraison (BL) | Delivery note | A document accompanying or recording a delivery. |
| Quantité commandée | Ordered quantity | Units requested in the order. |
| Quantité réceptionnée | Received quantity | Units physically delivered. |
| Quantité acceptée | Accepted quantity | Units approved for usable stock after inspection. |
| Quantité endommagée | Damaged quantity | Units received but not accepted as usable because they are damaged. |
| Quantité restante à recevoir | Quantity still awaiting delivery | Required units not yet physically received, after authorised amendments. |
| Écart de livraison | Delivery discrepancy | A difference in what was ordered and what arrived/was accepted. |
| Fournisseur | Supplier | Person or business providing goods/services. |
| Client | Customer | Person or business buying goods/services. |
| Partenaire commercial | Business partner | An organisation that may be a supplier, customer or both. |
| Gérant / responsable | Manager/person responsible | Person overseeing the process. |
| Comptable | Accountant | Person handling or checking accounting-related information. |
| Rôle | Role | A person's responsibilities in the process/system. |
| Traçabilité | Traceability/audit trail | Being able to explain what happened, when, why and who recorded it. |
| Correction / contrepassation | Correction/reversal | Fixing a posted mistake while preserving the original history. |
| Écart de stock | Stock discrepancy | Difference between recorded and observed quantities. |
| Exception métier | Business exception | A problem that needs follow-up beyond the expected workflow. |
| Dossier d'exception | Exception case | Record for one distinct problem and its follow-up. |
| Historique des actions | Action history | Dated sequence of significant updates and decisions. |
| Date/heure de l'opération | Event timestamp | When something actually happened. |
| Date/heure d'enregistrement | Record-entry timestamp | When it was entered into the system. |
| Date prévue | Expected date | When something is expected, not proof that it happened. |
| Prototype | Prototype | Early version used to test the design. |
| Cas de test | Test case | A scenario/input and expected result used to check behavior. |
| Cahier des charges | Requirements/specification | Document describing needs, expected functions and constraints. |
| PFE | End-of-study project | Formal project if required by the programme; confirm school rules. |
| Soutenance | Oral defence/presentation | Presentation in which the learner explains and defends the work. |

## Stock calculation to remember

`Stock final = stock initial + entrées acceptées − sorties enregistrées`

**Ending stock = starting stock + accepted incoming quantities − recorded outgoing quantities.** Placing an order does not itself add physical stock; receiving, accepting and posting are separate steps.
