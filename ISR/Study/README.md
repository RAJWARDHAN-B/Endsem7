# Information Storage and Retrieval: endsem study guide

BE IT Semester VII, 2019 pattern, subject 414441. These notes organize **eight retained 70-mark papers** by question topic, then extend them with related material from the ISR books. The explanations, worked solutions and examples are original; each embedded image has its source and license in its caption.

## Units

| Unit | Guide | Main themes |
|---|---|---|
| 3 | [Evaluation and visualization](unit-3-evaluation.md) | Precision, recall, F-score, E-measure, MRR, DCG/NDCG, relevance judgments, search interfaces |
| 4 | [Distributed and multimedia IR](unit-4-distributed-multimedia.md) | Source selection, partitioning, query processing, multimedia models, MULTOS, GEMINI |
| 5 | [Web searching](unit-5-web-search.md) | Search engines, crawling and indexing, ranking, hyperlinks, scraping |
| 6 | [Advanced IR](unit-6-advanced-ir.md) | XML retrieval, recommender systems, semantic web |

The papers generally offer **Q1 or Q2**, **Q3 or Q4**, **Q5 or Q6**, and **Q7 or Q8**. Those pairs broadly map to Units 3–6 respectively. Verify the instructions on your actual paper.

## Papers analyzed

These links point to the repository copies, which are currently Git LFS pointers in this checkout. Install Git LFS and hydrate them to open the PDFs. The paper content was analyzed using copies verified against the pointers' SHA-256 hashes.

| Code | Paper | Detailed answers |
|---|---|---|
| N22 | [Nov–Dec 2022](../PYQ/ISR_Endsem_2022_Nov-Dec.pdf) | [Answers](../PYQ/ISR_Endsem_2022_Nov-Dec_ans.md) |
| M23 | [May–Jun 2023 backlog](../PYQ/ISR_Endsem_2023_May-Jun_Backlog.pdf) | [Answers](../PYQ/ISR_Endsem_2023_May-Jun_Backlog_ans.md) |
| N23 | [Nov–Dec 2023](../PYQ/ISR_Endsem_2023_Nov-Dec.pdf) | [Answers](../PYQ/ISR_Endsem_2023_Nov-Dec_ans.md) |
| M24 | [May–Jun 2024 backlog](../PYQ/ISR_Endsem_2024_May-Jun_Backlog.pdf) | [Answers](../PYQ/ISR_Endsem_2024_May-Jun_Backlog_ans.md) |
| N24 | [Nov–Dec 2024](../PYQ/ISR_Endsem_2024_Nov-Dec.pdf) | [Answers](../PYQ/ISR_Endsem_2024_Nov-Dec_ans.md) |
| M25 | [May–Jun 2025](../PYQ/ISR_Endsem_2025_May-Jun.pdf) | [Answers](../PYQ/ISR_Endsem_2025_May-Jun_ans.md) |
| N25 | [Nov–Dec 2025](../PYQ/ISR_Endsem_2025_Nov-Dec.pdf) | [Answers](../PYQ/ISR_Endsem_2025_Nov-Dec_ans.md) |
| M26 | [May–Jun 2026](../PYQ/ISR_Endsem_2026_May-Jun.pdf) | [Answers](../PYQ/ISR_Endsem_2026_May-Jun_ans.md) |

M25 and N25 have substantially overlapping questions, with some differences; do not treat them as independent evidence of topic frequency.

## Question-to-topic map

Prompts below are **paraphrased**. `;` separates question parts; `/` separates the alternative questions. Follow the links above for detailed answers.

| Paper | Q1 / Q2 | Q3 / Q4 | Q5 / Q6 | Q7 / Q8 |
|---|---|---|---|---|
| N22 | Precision/recall numerical; performance measures; query specification / user-oriented measures; precision/recall; relevance judgments and feedback | Distributed architecture; partitioning / MULTOS; multimedia query languages | Web search; crawler-indexer; crawler strategies / hyperlinks; web characteristics; scraping | Recommenders and collaborative filtering; semantic web / text- vs data-centric XML; content-based recommendations |
| M23 | Evaluation and precision–recall trade-off; alternative measures; NDCG / user measures; MRR and F-score; visualization support | Distributed source selection; query processing / multimedia architecture; partitioning | Search engine; page ranking; Requests and Beautiful Soup / centralized vs distributed search; crawling and directories; scraping | Collaborative vs content filtering; recommender and collaborative filtering / text- vs data-centric XML; content-based recommendations |
| N23 | Precision/recall numerical; alternative measures; precision/recall / user measures; MRR and F-score; visualization support | Distributed source selection; multimedia IR model / multimedia architecture; partitioning | PageRank; Requests, Beautiful Soup and scraping / centralized vs distributed search; crawling and directories | Collaborative vs content filtering; XML vector space model / text- vs data-centric XML; content-based recommendations |
| M24 | Query specification; precision, recall and F-score / user measures; MRR, NDCG and E-measure | Distributed feature extraction; commercial DBMS multimedia support / GEMINI; MULTOS | Search engine; crawler-indexer; Requests and Beautiful Soup / scraping; ranking; crawler components | Text- vs data-centric XML; XML vector space model / content-based recommender; collaborative vs content filtering |
| N24 | Precision/recall numerical; NDCG; query specification / user measures; relevance judgments and pseudo feedback | Distributed architecture; partitioning / MULTOS; distributed query processing | Crawler-indexer; crawler role and web search / web characteristics; scraping | Collaborative recommender; XML retrieval challenges / text- vs data-centric XML; content-based recommendations |
| M25 | MRR and NDCG; numerical; precision and recall / user measures; DCG and F-score; query specification | Multimedia data modelling; commercial DBMS support / GEMINI; MULTOS | Search engine; ranking; Requests and Beautiful Soup / scraping; crawler-indexer; web search challenges | Content-based recommender; XML vector space model / content-based document recommendations; collaborative vs content filtering |
| N25 | MRR and NDCG; numerical; query specification / user measures; DCG and F-score; precision and recall | Multimedia data modelling; MULTOS / GEMINI; commercial DBMS support | Search engine; crawler-indexer; web challenges / scraping; ranking; Requests and Beautiful Soup | Content-based recommender; XML vector space model / content-based document recommendations; collaborative vs content filtering |
| M26 | Query specification; precision and recall; user measures / visualization support; MRR and F-score; judgments and feedback | Distributed feature extraction; partitioning / commercial DBMS support; GEMINI | Crawler-indexer; scraping; Requests and Beautiful Soup / ranking; web search challenges; hyperlinks | Collaborative vs content filtering; text- vs data-centric XML / collaborative recommender; XML vector space model |

## How to use

1. Learn the definition, follow the worked example, and practice explaining each figure without looking.
2. Use the linked PYQ codes to practice the actual variants, including every subpart.
3. Use comparisons for 8–9 mark answers; include an example, working, advantages and limitations where applicable.
4. Images are stored locally for offline Markdown preview. Book references link to specific **PDF viewer pages**, not printed page numbers; if page fragments do not work in your viewer, enter the page manually.
5. Repeated questions indicate useful practice, not a guarantee of exam questions or complete syllabus coverage.

**Primary reference:** [Decode ISR, Units 3–6](../Books/ISR_Decode_Units03-06.pdf). Additional explanations: [Technical](../Books/ISR_Technical_Units03-06.pdf), [TechKnowledge](../Books/ISR_TechKnowledge_Units03-06.pdf), and [TechNeo](../Books/ISR_TechNeo_Units03-06.pdf). Specific figures from the repository books are linked to their PDF pages, not reproduced inline.
