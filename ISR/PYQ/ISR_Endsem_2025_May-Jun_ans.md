# ISR: 2025 May-Jun — detailed answers

[Question paper](ISR_Endsem_2025_May-Jun.pdf) | [ISR study index](../Study/README.md)

Question headings are paraphrased; both sides of each OR are answered. Examples are illustrative unless identified as paper data. The paper PDF may require Git LFS hydration. Book links use PDF viewer page numbers.

## Q1(a) — MRR and NDCG

| Measure | What it evaluates | Key point |
|---|---|---|
| Precision@k | Relevant results in top k divided by k | Useful for a fixed-size first page; specify k |
| Average precision (AP) | Average of P@rank over ranks containing relevant items, divided by total relevant items | Rewards placing multiple relevant results early |
| Mean average precision (MAP) | Mean AP over queries | Uses binary judgments and captures ranking over queries |
| Reciprocal rank (RR) | `1 / rank of first relevant result` | Measures how soon the first answer appears |
| MRR | Mean RR across queries | Useful for a single satisfactory answer |
| DCG / NDCG | Discounted graded relevance | Rewards highly relevant items near the top |

**MRR example:** first relevant result at ranks 1, 2 and 4 for three queries gives `MRR = (1 + 1/2 + 1/4)/3 ≈ 0.583`. If a query has no relevant result in the evaluated list, its RR is conventionally zero. MRR does not reward additional relevant results after the first.

**AP example:** suppose four retrieved results have binary relevance `[1, 0, 1, 0]`, and the collection contains three relevant items total. Relevant items occur at ranks 1 and 3, with `P@1 = 1` and `P@3 = 2/3`; `AP = (1 + 2/3)/3 ≈ 0.556`. The third relevant item was missed, so it remains in the denominator.

#### DCG and NDCG worked example

For a cutoff `k`, one common convention is `DCG@k = Σ(i=1..k) (2^rel_i − 1) / log₂(i + 1)`, where `rel_i` is a graded relevance score. Other courses may use raw relevance instead of `2^rel − 1`; use the convention required by the question consistently.

Suppose the first three results have grades `[3, 0, 2]`:

| Rank | Grade | Gain `2^grade − 1` | Discounted gain |
|---|---:|---:|---:|
| 1 | 3 | 7 | `7/log₂2 = 7` |
| 2 | 0 | 0 | `0/log₂3 = 0` |
| 3 | 2 | 3 | `3/log₂4 = 1.5` |

`DCG@3 = 8.5`. The ideal ordering of these same three judged items is `[3, 2, 0]`, so `IDCG@3 = 7 + 3/log₂3 ≈ 8.893`. Thus `NDCG@3 = DCG/IDCG ≈ 0.956`. In a full test collection, compute the ideal ordering from all judged candidate documents, not merely from the returned three. If IDCG is zero, state the chosen evaluation convention.

**References:**
- [Decode ISR, unit 3, PDF page 5](../Books/ISR_Decode_Units03-06.pdf#page=5).
- [ISR Unit 3 study notes](../Study/unit-3-evaluation.md).

## Q1(b) — Calculate precision and recall for 80 topic records and 60 retrieved

Of 60 retrieved records, 45 are relevant. **Precision** = 45/60 = **75%**.

If all 80 records on the topic are relevant, **recall** = 45/80 = **56.25%**, with TP = 45, FP = 15 and FN = 35. The paper does not explicitly state that all 80 are relevant, so this assumption must be stated; otherwise the total number of relevant records, and hence recall, is unknown.

![Precision and recall shown on a relevance versus retrieval matrix](../Study/images/precision-recall.jpg)

*Precision and recall by kindlychung, [Wikimedia Commons / Openclipart](https://commons.wikimedia.org/wiki/File:Precision_recall.svg), [CC0 / public domain](https://creativecommons.org/publicdomain/zero/1.0/); rasterized and converted to JPEG with a white background. Interpret “predicted positive” as “retrieved” and “ground-truth positive” as “relevant.”*

**References:**
- [Decode ISR, unit 3, PDF page 3](../Books/ISR_Decode_Units03-06.pdf#page=3).
- [ISR Unit 3 study notes](../Study/unit-3-evaluation.md).

## Q1(c) — Precision and recall

An information retrieval (IR) system searches a document collection for an **information need** expressed as a query. Evaluation asks how well the returned results meet that need, not just how quickly the software runs.

An offline test collection normally includes documents, representative queries and **relevance judgments**. The judgments serve as the reference against which systems are compared. A fair comparison uses the same queries and judgments, the same cutoff, and reports performance across queries. Operational evaluation can also consider latency, cost and usability; no one measure captures every goal.

| | Relevant to query | Not relevant |
|---|---:|---:|
| Retrieved | True positive (TP) | False positive (FP) |
| Not retrieved | False negative (FN) | True negative (TN) |

![Precision and recall shown on a relevance versus retrieval matrix](../Study/images/precision-recall.jpg)

*Precision and recall by kindlychung, [Wikimedia Commons / Openclipart](https://commons.wikimedia.org/wiki/File:Precision_recall.svg), [CC0 / public domain](https://creativecommons.org/publicdomain/zero/1.0/); rasterized and converted to JPEG with a white background. Interpret “predicted positive” as “retrieved” and “ground-truth positive” as “relevant.”*

For the book's Venn diagrams of relevant and retrieved sets, see [PDF page 3](../Books/ISR_Decode_Units03-06.pdf#page=3).

**Precision = TP / (TP + FP)** = relevant retrieved / all retrieved. It answers: “Of what I returned, how much is useful?”

**Recall = TP / (TP + FN)** = relevant retrieved / all relevant. It answers: “Of all useful items, how many did I find?”

If nothing is retrieved, precision's denominator is zero; if there are no relevant items, recall's denominator is zero. State the evaluation convention instead of dividing by zero. True negatives are usually huge in IR, so accuracy alone can be misleading.

**Example:** if 20 results contain 15 relevant items and 30 relevant items exist in total, precision is 15/20 = 75% and recall is 15/30 = 50%. Precision assesses result quality; recall assesses coverage.

**References:**
- [Decode ISR, unit 3, PDF page 3](../Books/ISR_Decode_Units03-06.pdf#page=3).
- [ISR Unit 3 study notes](../Study/unit-3-evaluation.md).

## Q2(a) — User-oriented measures

System metrics use judgments and ranked results; user-oriented measures consider the searcher's **actual task and experience**. Measure on representative users and tasks, with clear conditions and consent.

| Measure | How it is observed | Why it matters |
|---|---|---|
| Task success / answer correctness | Whether the task or answer meets defined criteria | Measures the practical outcome |
| Time to first useful result / completion | Time from task start to useful result or completion | Measures effort and delay |
| Interaction effort | Number of queries, clicks, reformulations, pages inspected | Captures workload; fewer clicks alone need not mean better |
| Satisfaction / perceived relevance | Questionnaire or rating after task | Captures subjective experience |
| Coverage and novelty | Useful distinct information found, including new items | Helps exploratory searches |
| Accessibility and usability | Observed ability to use controls, including keyboard and assistive technology | Enables different users to search effectively |

Clicks and dwell time are **proxies**, affected by presentation and position bias, not guaranteed judgments. Combine behavioral data with feedback and outcomes.

#### Textbook user-oriented ratios

The book also defines measures relative to what the user already knows or expects. Let `R` be relevant documents, `A` retrieved documents and `K` the documents already known to the user:

| Measure | Definition | Interpretation |
|---|---|---|
| Coverage ratio | `|R ∩ A ∩ K| / |R ∩ K|` | Fraction of the known relevant documents that were retrieved |
| Novelty ratio | `|(R ∩ A) \ K| / |R ∩ A|` | Fraction of relevant retrieved documents that were previously unknown to the user |
| Relative recall | Relevant documents found / number of relevant documents the user expected to find | Compares actual discoveries to the user's expectation, not necessarily to the true total |
| Recall effort | Number of relevant documents the user expected to find / number of documents examined in the attempt | Relates the user's expected yield to examination effort; state the examination stopping point |

**Example:** suppose the user knows four relevant documents, the system retrieves three of them, and it also retrieves two previously unknown relevant documents. Coverage is `3/4 = 75%`; novelty is `2/5 = 40%`. If the user expected four relevant documents and found five, relative recall is `5/4 = 1.25` under this definition; unlike ordinary recall, it may exceed one. If ten documents were examined to complete the search, recall effort is `4/10 = 0.4`. These ratios require nonzero denominators and a clearly specified user, query and assessment procedure.

See the textbook's [user-oriented measures and diagram, PDF pages 12–13](../Books/ISR_Technical_Units03-06.pdf#page=12). Different sources may define user-centric measures differently, so state the chosen convention.

**Example:** give users the same task of finding a relevant research paper. Measure time to a correct paper, task success, number of reformulations and a satisfaction rating. A fast answer is not useful if it is wrong; compare measures together.

**References:**
- [Decode ISR, unit 3, PDF page 6](../Books/ISR_Decode_Units03-06.pdf#page=6).
- [ISR Unit 3 study notes](../Study/unit-3-evaluation.md).
- [Technical: user-oriented ratios, pages 12–13](../Books/ISR_Technical_Units03-06.pdf#page=12).

## Q2(b) — DCG and F-score

| Measure | What it evaluates | Key point |
|---|---|---|
| Precision@k | Relevant results in top k divided by k | Useful for a fixed-size first page; specify k |
| Average precision (AP) | Average of P@rank over ranks containing relevant items, divided by total relevant items | Rewards placing multiple relevant results early |
| Mean average precision (MAP) | Mean AP over queries | Uses binary judgments and captures ranking over queries |
| Reciprocal rank (RR) | `1 / rank of first relevant result` | Measures how soon the first answer appears |
| MRR | Mean RR across queries | Useful for a single satisfactory answer |
| DCG / NDCG | Discounted graded relevance | Rewards highly relevant items near the top |

**MRR example:** first relevant result at ranks 1, 2 and 4 for three queries gives `MRR = (1 + 1/2 + 1/4)/3 ≈ 0.583`. If a query has no relevant result in the evaluated list, its RR is conventionally zero. MRR does not reward additional relevant results after the first.

**AP example:** suppose four retrieved results have binary relevance `[1, 0, 1, 0]`, and the collection contains three relevant items total. Relevant items occur at ranks 1 and 3, with `P@1 = 1` and `P@3 = 2/3`; `AP = (1 + 2/3)/3 ≈ 0.556`. The third relevant item was missed, so it remains in the denominator.

#### DCG and NDCG worked example

For a cutoff `k`, one common convention is `DCG@k = Σ(i=1..k) (2^rel_i − 1) / log₂(i + 1)`, where `rel_i` is a graded relevance score. Other courses may use raw relevance instead of `2^rel − 1`; use the convention required by the question consistently.

Suppose the first three results have grades `[3, 0, 2]`:

| Rank | Grade | Gain `2^grade − 1` | Discounted gain |
|---|---:|---:|---:|
| 1 | 3 | 7 | `7/log₂2 = 7` |
| 2 | 0 | 0 | `0/log₂3 = 0` |
| 3 | 2 | 3 | `3/log₂4 = 1.5` |

`DCG@3 = 8.5`. The ideal ordering of these same three judged items is `[3, 2, 0]`, so `IDCG@3 = 7 + 3/log₂3 ≈ 8.893`. Thus `NDCG@3 = DCG/IDCG ≈ 0.956`. In a full test collection, compute the ideal ordering from all judged candidate documents, not merely from the returned three. If IDCG is zero, state the chosen evaluation convention.

`F1 = 2PR / (P + R)` is the harmonic mean of precision `P` and recall `R`. It is high only when both are high. With `P = 0.75` and `R = 0.5625`, `F1 ≈ 0.643` or **64.3%**.

`Fβ = (1 + β²)PR / (β²P + R)`. For this standard convention, `β > 1` emphasizes recall; `β < 1` emphasizes precision. With `β = 1`, it becomes F1. When both P and R are zero, F1 is commonly defined as zero by evaluation convention.

The complementary **E-measure** is `Eβ = 1 − Fβ`; lower is better. Always show the exact formula or convention used, because texts sometimes parameterize the precision/recall weight differently.

**References:**
- [Decode ISR, unit 3, PDF page 5](../Books/ISR_Decode_Units03-06.pdf#page=5).
- [ISR Unit 3 study notes](../Study/unit-3-evaluation.md).

## Q2(c) — Query-specification techniques

Information visualization presents documents, relationships or results visually to help users navigate and interpret them. A search interface supports the full cycle:

1. **Start:** suggest examples, recent searches, categories, collections or overviews rather than leaving a user with only a blank box.
2. **Specify:** allow keywords, phrases, Boolean operators, filters and other controls.
3. **Inspect:** show titles, snippets with highlighted terms, dates, source and useful metadata; preview full context.
4. **Refine:** support facets, query editing, related terms and relevance feedback.
5. **Understand:** use ranked lists, timelines, clusters, maps or link views where the visualization suits the data. Provide legends and accessible text alternatives.

| Query technique | Example | Benefit / limitation |
|---|---|---|
| Keyword or phrase | `"information retrieval"` | Fast and familiar; ambiguous terms may need refinement |
| Boolean | `(image OR video) AND retrieval NOT medical` | Explicit set logic; precedence and syntax can be difficult |
| Faceted | Filter by year, type and author after a query | Easy progressive narrowing; depends on reliable metadata |
| Form / fielded | Title contains “web”; year ≥ 2022 | Makes structure explicit; users need to know fields |
| Query by example | Upload an image similar to the desired item | Useful when words are hard to specify; similarity can miss meaning |
| Natural language | “Find recent papers on image search” | Accessible, but interpretation can be ambiguous |
| Direct visual selection | Select a region on a map or drag a range on a timeline | Supports exploration; must be usable without relying only on color |

#### Graphical query specification

A **query** is a representation of an information need that the system can process. Query specification includes choosing the collection or fields as well as expressing the terms and their relationships. A graphical interface can make these relationships visible rather than requiring users to remember a query language.

- **Boolean query:** `("image" OR "video") AND retrieval` finds documents containing retrieval and at least one of the media terms. Parentheses make the intended grouping explicit; exact Boolean matching need not rank the matches.
- **Faceted query:** first search for `retrieval`, then select media type = image and year = 2024. The selected values narrow the result set; the user can remove a facet to broaden it again.
- **Form filling and menus:** enter `retrieval` in the title field and choose a year from a menu. Fields expose the available metadata, although an appropriate field must exist.
- **Venn diagrams and VQuery:** represent terms by circles or ovals. Overlapping regions show combinations of terms; selecting the overlap of `image` and `retrieval` specifies their AND. VQuery lets users position term ovals and select regions. Counts can help the user see how restrictive a combination is.
- **Natural language and free text:** a user writes “find recent papers on image retrieval”; the system interprets the words rather than requiring explicit Boolean operators. Interpretation can be ambiguous.
- **Direct manipulation:** users interact with visible objects through incremental, reversible actions with immediate feedback. Moving an oval or choosing a facet lets them revise their query without typing a complex expression.

See the textbook's [VQuery diagram, PDF page 18](../Books/ISR_Technical_Units03-06.pdf#page=18), and [query specification discussion, pages 15–17](../Books/ISR_Technical_Units03-06.pdf#page=15). For an exam answer, define the query, explain at least three techniques with examples, and describe how the interface makes refinement easier.

#### Showing document context and result sets

These techniques help users **inspect results**, rather than all being ways to formulate a query:

| Technique | What it shows | Example and use |
|---|---|---|
| Document surrogate | A compact substitute such as title, author, date and snippet | A user scans a result list before opening full documents; snippets can omit important context. |
| KWIC (keyword in context) | Each query-term occurrence with nearby words | For `retrieval`, show “…image **retrieval** using texture…” so the reader can judge the sense of the match. |
| TileBars | Query-term or term-group frequencies across consecutive document sections | Rows correspond to terms or groups, columns to sections; darker tiles indicate more occurrences. Overlap helps identify sections discussing multiple terms. Clicking a tile can open that section. |
| SeeSoft | Compact lines of text with visual highlighting | Shows the distribution of matches across a long text; users zoom in for details. |
| InfoCrystal | Counts of documents matching different combinations of query terms | Also works as a visual query language: select term combinations instead of writing complex Boolean expressions. |
| SuperBook | A document's table of contents alongside its content | Expanding sections helps locate hits while preserving the document's hierarchy. |

For example, if a document has three sections and the TileBar row for `image` is dark only in section 1 while the row for `retrieval` is dark in sections 1 and 3, section 1 is a promising place to inspect both terms. TileBars show **distribution, not meaning or guaranteed relevance**. Do not confuse them with interface title bars or with VQuery's query-specification diagram.

![Illustrative TileBar for two query terms across three sections](../Study/images/tilebars-example.svg)

*Original illustrative diagram for this guide; the shades represent relative term frequency, not exact counts.*

See the book's [KWIC figure, page 19](../Books/ISR_Technical_Units03-06.pdf#page=19), [TileBars description, page 20](../Books/ISR_Technical_Units03-06.pdf#page=20), and [InfoCrystal and SuperBook, page 21](../Books/ISR_Technical_Units03-06.pdf#page=21).

**References:**
- [Decode ISR, unit 3, PDF page 7](../Books/ISR_Decode_Units03-06.pdf#page=7).
- [ISR Unit 3 study notes](../Study/unit-3-evaluation.md).
- [Technical: query specification and VQuery, page 15](../Books/ISR_Technical_Units03-06.pdf#page=15); [VQuery figure, page 18](../Books/ISR_Technical_Units03-06.pdf#page=18); [TileBars, page 20](../Books/ISR_Technical_Units03-06.pdf#page=20).

## Q3(a) — Data modelling in multimedia IR

**Multimedia IR** retrieves image, audio, video, text or combinations of these in response to a query, often using similarity rather than exact equality. In a content-based image search, the user submits a sample picture; the system extracts its visual features and ranks stored images with similar features.

![Content-based image retrieval indexes image features and compares a query image to stored signatures](../Study/images/cbir.jpg)

*Content-based image retrieval schema by Xiawi, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Schema_of_content-based_image_retrieval_%28CBIR%29.png), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); converted to JPEG with a white background. “Metadata” here refers to extracted image descriptors/signatures, not only manually supplied captions.*

#### Architecture and stages

1. **Ingest and store** multimedia objects with identifiers, media type, metadata and access permissions.
2. **Extract features:** color, shape and texture for images; spectral or temporal features for sound; frames, motion and audio for video. Some systems also use captions or learned embeddings.
3. **Index** feature vectors and textual metadata so that the system can find candidate objects efficiently.
4. **Formulate a query:** text, attributes, an example image/audio clip, sketches, spatial relations or a combination.
5. **Match and rank:** compare query and indexed descriptors using a suitable distance or similarity; apply any exact metadata filters.
6. **Present results and gather feedback:** show thumbnails or playable previews; allow users to mark relevance and refine.

**Semantic gap:** similar low-level features do not guarantee the same meaning. A blue sea and a blue car might have similar dominant colors but different subjects. Feature quality, computation, large storage needs and privacy are practical limitations.

#### Data modelling

A multimedia data model describes both **logical objects** and their internal representation: object ID, type, metadata, components, features, relationships and access rights. A video can have a title, duration, scenes, frames and audio tracks; timestamps preserve temporal relationships. An image can have regions, captions and feature vectors.

| Query predicate | Example |
|---|---|
| Attribute | Videos with duration under five minutes |
| Content / similarity | Images visually similar to a sample |
| Spatial | A person to the left of a vehicle |
| Temporal | A sound occurs before a scene change |
| Semantic | Pictures containing a bicycle, based on annotations or a classifier |

Exact field matches and approximate similarity scores may be combined. Feature extraction and semantic labels can be uncertain; a score is not a guarantee of true meaning.

Consider a five-minute wildlife video: the model stores its ID, title and duration, links it to audio and video tracks, and assigns timestamps to scenes. Extracted visual descriptors describe frames; recognized speech or captions provide text. A request for “birds near water in the first minute” combines a temporal restriction with uncertain visual or text-based evidence. The system should return a ranked clip and enough context to inspect it, rather than pretending the recognition is exact.

#### Multimedia query language

A multimedia query language needs a way to specify an example or features, metadata restrictions, spatial/temporal relationships and possibly weights or similarity thresholds. Processing parses the request, filters or indexes candidates, computes similarity, ranks results and supports refinement. Unlike a conventional exact database selection, an approximate query may return graded matches.

Example: “Show clips shorter than 30 seconds in which a vehicle appears **before** a pedestrian; rank by similarity to this sample.” Duration is an exact filter; recognition and similarity may be approximate. Results can vary with the feature model and threshold.

**References:**
- [Decode ISR, unit 4, PDF page 23](../Books/ISR_Decode_Units03-06.pdf#page=23).
- [ISR Unit 4 study notes](../Study/unit-4-distributed-multimedia.md).

## Q3(b) — Multimedia support in commercial DBMS

![Content-based image retrieval indexes image features and compares a query image to stored signatures](../Study/images/cbir.jpg)

*Content-based image retrieval schema by Xiawi, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Schema_of_content-based_image_retrieval_%28CBIR%29.png), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); converted to JPEG with a white background. “Metadata” here refers to extracted image descriptors/signatures, not only manually supplied captions.*

A DBMS can store or reference media and manage associated structured metadata:

- **BLOB** for binary data such as an image; **CLOB** for large text. A database may instead store a secure file/object-store reference.
- Tables and indexes for IDs, titles, dates, ownership and permissions.
- Object-relational features, user-defined types and functions for structured or application-specific descriptors.
- Text, spatial or vector indexes and extensions where the particular product supports them.
- Transactions, access control, backup and recovery for consistent management.

Example: a `Media` table stores an ID, title, timestamp, a BLOB or object URL, and an image-feature vector. A metadata filter narrows the candidate set, then an appropriate similarity function ranks the candidates. **Storing a BLOB does not itself enable visual search**: extraction, similarity computation and suitable indexing must be supplied.

Product-specific names, limits and multimedia extensions vary by product and version. Older book examples are historical; do not assume every DBMS supports the same media operations.

**References:**
- [Decode ISR, unit 4, PDF page 25](../Books/ISR_Decode_Units03-06.pdf#page=25).
- [ISR Unit 4 study notes](../Study/unit-4-distributed-multimedia.md).

## Q4(a) — Multimedia IR and GEMINI

**Multimedia IR** retrieves image, audio, video, text or combinations of these in response to a query, often using similarity rather than exact equality. In a content-based image search, the user submits a sample picture; the system extracts its visual features and ranks stored images with similar features.

![Content-based image retrieval indexes image features and compares a query image to stored signatures](../Study/images/cbir.jpg)

*Content-based image retrieval schema by Xiawi, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Schema_of_content-based_image_retrieval_%28CBIR%29.png), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); converted to JPEG with a white background. “Metadata” here refers to extracted image descriptors/signatures, not only manually supplied captions.*


**GEMINI** (GEneric Multimedia INdexIng) accelerates similarity search by first filtering objects in a lower-dimensional **feature space** and then checking surviving candidates using the original distance. See [book PDF pages 33–34](../Books/ISR_Decode_Units03-06.pdf#page=33).

For query `q`, object `x` and distance threshold `ε`:

1. Choose an original distance `D(q,x)` appropriate for the media.
2. Map each object and the query to a compact feature vector `f(x)`.
3. Index stored features using a suitable spatial access method.
4. Find candidates whose **feature-space lower-bound distance** `d(f(q),f(x)) ≤ ε`.
5. Compute the original distance for each candidate and return only objects with `D(q,x) ≤ ε`.

The no-false-dismissal guarantee requires `d(f(q), f(x)) ≤ D(q,x)` for every pair under the chosen transformation and distances. A candidate may pass the inexpensive filter and fail the exact check: that is a **false positive**, which the second stage removes. If the lower-bound property is absent, exact recall is not guaranteed.

**Small example:** let `q = (1,2)`, `x = (2,3)`, original distance be Euclidean, and feature be the first coordinate. The feature distance is `|1−2| = 1`, while the full distance is `√2 ≈ 1.414`. With `ε = 1.2`, `x` passes the feature filter but is rejected by the full comparison. With `ε = 1.5`, it passes both. Using the first-coordinate distance is a lower bound on full Euclidean distance.

**Benefits:** avoids expensive full comparisons for many objects and separates the generic indexing method from media-specific features. **Limitations:** weak features yield many false positives; dimensionality and index overhead can reduce the benefit; guarantees depend on the distance bound.

**References:**
- [Decode ISR, unit 4, PDF page 33](../Books/ISR_Decode_Units03-06.pdf#page=33).
- [ISR Unit 4 study notes](../Study/unit-4-distributed-multimedia.md).

## Q4(b) — MULTOS

**MULTOS** is a historical **MULTimedia Office Server**, a client–server document-management system designed to file and retrieve complex multimedia office documents. It models document collections, document types, document attributes and the internal organization of a document, rather than treating every document as one undifferentiated string.

| View | What it describes | Letter example |
|---|---|---|
| Logical structure | Content organization | Letter, heading, body, signature |
| Layout structure | Presentation on pages | Pages, frames, positions |
| Conceptual structure | Domain-specific meaning and relationships | Sender, recipient, address, date |

**Working:** a client creates or requests a document; a document server stores the object, type, attributes and components; a query may combine attributes and content; matching documents or components are retrieved and presented. A type can constrain what components an instance contains. For example, a letter type can include sender and recipient; the corresponding components of a particular letter contain their actual values. The book illustrates a conceptual letter structure on [PDF page 28](../Books/ISR_Decode_Units03-06.pdf#page=28).

**Why useful:** structured retrieval can locate a letter by sender, its text, or a component. **Limitations:** models and clients must agree on document structure; managing diverse media, permissions and efficient similarity search adds complexity. Distinguish the historical MULTOS model from generic modern database features.

For example, the query “letters from Patil about retrieval” combines a sender attribute with a content condition. The server identifies matching document instances and returns the selected document or component; a client presents it according to the stored layout. Logical structure describes *what parts exist*, layout describes *how they appear*, and conceptual structure relates parts to *domain meaning*. These views are complementary rather than three separate documents.

**References:**
- [Decode ISR, unit 4, PDF page 27](../Books/ISR_Decode_Units03-06.pdf#page=27).
- [ISR Unit 4 study notes](../Study/unit-4-distributed-multimedia.md).

## Q5(a) — Search-engine mechanism

The **web** is a collection of resources identified by URLs and connected by hyperlinks. Resources include text, images, multimedia and structured data, provided by many independent owners. The web is large, heterogeneous, dynamic, multilingual, partly duplicated and partly inaccessible to crawlers. It includes spam and pages whose contents require authentication, forms or other interaction.

An example search-engine workflow:

1. **Discovery and crawling:** start with seed URLs, download allowed pages and discover more links.
2. **Processing:** parse documents, extract text, metadata and links, remove or identify duplicates, and normalize terms.
3. **Indexing:** build an inverted index mapping each term to the documents (and often positions) containing it.
4. **Query processing:** tokenize the user's query, interpret spelling or intent, and retrieve candidate documents from the index.
5. **Ranking:** score candidates using relevance signals, possibly including text, links, freshness and other factors.
6. **Presentation:** show ranked titles, URLs and snippets; support filtering, reformulation and feedback.

For example, a crawler discovers a university's public course page and the indexer associates its terms with its document ID. Later, the query `information retrieval` retrieves candidate IDs from the index; the ranker orders candidates and the interface displays titles and snippets. **Offline** crawling/indexing and **online** query processing are different phases: the engine does not normally crawl the entire web for every query.

**Example inverted index:** if document D1 contains “web retrieval” and D2 contains “image retrieval”, postings for `retrieval` include D1 and D2, while `web` points to D1. For `web retrieval`, the engine can efficiently identify D1 without scanning every document at query time.

| Search engine | Web directory | Meta-searcher |
|---|---|---|
| Crawls or receives pages and indexes them | Organizes selected resources into categories, often curated | Sends a query to multiple search services and merges their responses |
| Broad keyword search | Browsing by subject | Wider coverage without necessarily maintaining its own full index |
| May contain stale or low-quality pages | Human curation can be costly and incomplete | Dependent on providers and difficult score merging |

#### Challenges in web search

- **Scale and speed:** huge collections require distributed storage, indexing and low query latency.
- **Change and freshness:** pages appear, move, change or disappear; recrawling everything immediately is impractical.
- **Quality and spam:** duplicate pages, manipulation and misleading content degrade results.
- **Heterogeneity:** multiple languages, formats, scripts and media complicate parsing and relevance.
- **Ambiguity:** short queries such as `java` can mean a programming language, island or coffee.
- **Coverage:** authenticated, dynamically generated, blocked or unlinked resources may not be crawled; absence from the index is not proof that a page does not exist.
- **Privacy and fairness:** user data and ranking choices require careful handling.

![Web crawler architecture showing a scheduler, URL queue, downloader, and storage](../Study/images/crawler.jpg)

*Web crawler architecture, vector version by dnet based on Carlos Castillo's diagram, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:WebCrawlerArchitecture.svg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); rasterized and converted to JPEG with a white background. Storage can feed an indexer, a separate step not shown in this figure.*

The figure depicts crawling; the indexer, query processor and ranker described above complete the search-engine mechanism. The textbook's [distributed crawler–indexer diagram](../Books/ISR_Decode_Units03-06.pdf#page=48) provides another architecture.

**References:**
- [Decode ISR, unit 5, PDF page 41](../Books/ISR_Decode_Units03-06.pdf#page=41).
- [ISR Unit 5 study notes](../Study/unit-5-web-search.md).

## Q5(b) — Ranking and its importance

**Ranking** orders candidate results so the most useful are likely to appear first. It matters because users often inspect only the first few results. A search score can incorporate query–document text similarity, term location, page quality, freshness and other signals. Different systems use different signals; ranking is not synonymous with PageRank.

**PageRank** is a link-based measure motivated by a random web surfer: a page receives importance from incoming links, particularly from important pages. Each linking page divides its contribution across outgoing links. A damping factor allows a random jump to any page, preventing the surfer from remaining trapped in a link structure.

![A link graph with example PageRank values, showing importance flows through incoming links](../Study/images/pagerank.jpg)

*Illustrative PageRank graph by 345Kai and Stannered, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:PageRanks-Example.svg), public domain; rasterized and converted to JPEG with a white background. Percentages describe this particular graph and damping setting, not general web traffic.*

`PR(A) = (1−d)/N + d × Σ[PR(T) / outdegree(T)]`, summing over pages `T` linking to A; `N` is the number of pages, and `d` is commonly set to 0.85. For dangling pages with no outgoing links, redistribute their rank according to the chosen teleportation distribution, commonly uniformly. Start with equal ranks and iterate until the scores converge.

**One iteration:** three pages start at `1/3`; A links to B, B links to A and C, and C links to A. With `d = 0.85`, base contribution is `0.15/3 = 0.05`:

| Page | Incoming contributions | Updated rank |
|---|---|---:|
| A | B contributes `1/6`, C contributes `1/3` | `0.05 + 0.85(1/6 + 1/3) = 0.475` |
| B | A contributes `1/3` | `0.05 + 0.85/3 ≈ 0.333` |
| C | B contributes `1/6` | `0.05 + 0.85/6 ≈ 0.192` |

These are **first-iteration** values, not the converged final scores. A highly linked page is not necessarily relevant, reliable or current for a given query; link spam can manipulate signals. Explain PageRank alongside query relevance rather than claiming it is the only ranking criterion.

**References:**
- [Decode ISR, unit 5, PDF page 50](../Books/ISR_Decode_Units03-06.pdf#page=50).
- [ISR Unit 5 study notes](../Study/unit-5-web-search.md).

## Q5(c) — Requests and Beautiful Soup

**Web scraping** extracts selected data from pages, typically by fetching HTML and parsing its structure. Crawling discovers and fetches pages, while scraping extracts desired fields; a project may use both.

For example, to collect public product names and prices: verify access terms and any available API, request allowed pages at a polite rate, parse each listing, extract name and price, validate the extracted values, and store them with a source and timestamp. Layout changes, JavaScript-rendered content, inaccessible pages and inconsistent markup can break scrapers.

| Tool | Purpose | Important detail |
|---|---|---|
| Python `requests` | Makes HTTP requests and exposes status, headers and response body | Set timeouts; call `raise_for_status()` to surface HTTP errors |
| Beautiful Soup (`bs4`) | Parses HTML/XML and provides tag/CSS selection | Parse the returned HTML; it does not fetch pages or execute JavaScript |

Minimal illustrative code, assuming dependencies are installed and the site permits access:

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com/", timeout=10)
response.raise_for_status()
document = BeautifulSoup(response.text, "html.parser")
heading = document.select_one("h1")
if heading is None:
    raise ValueError("Expected page heading was not found")
print(heading.get_text(strip=True))
```

In an exam, describe request, status check, parsing, selection and extraction separately. Avoid bypassing login, access restrictions, rate limits or technical barriers; do not collect personal data unnecessarily. HTML can change, so a selector should be checked and errors reported.

**References:**
- [Decode ISR, unit 5, PDF page 58](../Books/ISR_Decode_Units03-06.pdf#page=58).
- [ISR Unit 5 study notes](../Study/unit-5-web-search.md).

## Q6(a) — Web scraping

**Web scraping** extracts selected data from pages, typically by fetching HTML and parsing its structure. Crawling discovers and fetches pages, while scraping extracts desired fields; a project may use both.

For example, to collect public product names and prices: verify access terms and any available API, request allowed pages at a polite rate, parse each listing, extract name and price, validate the extracted values, and store them with a source and timestamp. Layout changes, JavaScript-rendered content, inaccessible pages and inconsistent markup can break scrapers.

| Tool | Purpose | Important detail |
|---|---|---|
| Python `requests` | Makes HTTP requests and exposes status, headers and response body | Set timeouts; call `raise_for_status()` to surface HTTP errors |
| Beautiful Soup (`bs4`) | Parses HTML/XML and provides tag/CSS selection | Parse the returned HTML; it does not fetch pages or execute JavaScript |

Minimal illustrative code, assuming dependencies are installed and the site permits access:

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com/", timeout=10)
response.raise_for_status()
document = BeautifulSoup(response.text, "html.parser")
heading = document.select_one("h1")
if heading is None:
    raise ValueError("Expected page heading was not found")
print(heading.get_text(strip=True))
```

In an exam, describe request, status check, parsing, selection and extraction separately. Avoid bypassing login, access restrictions, rate limits or technical barriers; do not collect personal data unnecessarily. HTML can change, so a selector should be checked and errors reported.

**References:**
- [Decode ISR, unit 5, PDF page 56](../Books/ISR_Decode_Units03-06.pdf#page=56).
- [ISR Unit 5 study notes](../Study/unit-5-web-search.md).

## Q6(b) — Crawler–indexer architecture

A **web crawler** automatically discovers and fetches web resources to build or refresh a collection. It does not itself decide that a page is relevant to every user's query; the indexer and ranking components handle other parts of search.

![Web crawler architecture showing a scheduler, URL queue, downloader, and storage](../Study/images/crawler.jpg)

*Web crawler architecture, vector version by dnet based on Carlos Castillo's diagram, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:WebCrawlerArchitecture.svg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); rasterized and converted to JPEG with a white background. Storage can feed an indexer, a separate step not shown in this figure.*

#### Components and operation

1. **Seed URLs:** known starting pages.
2. **URL frontier / queue:** discovered URLs awaiting a fetch; avoids repeatedly scheduling identical normalized URLs.
3. **Scheduler:** chooses the next URL, observes site policies and spacing, and prioritizes important or stale content.
4. **DNS resolver and fetcher:** resolve the host and retrieve the allowed resource over HTTP(S), subject to timeouts and error handling.
5. **Parser / link extractor:** extract text, metadata and outgoing URLs; resolve relative links against the page URL.
6. **Duplicate detection and filters:** avoid repeated content and disallowed URL patterns; add suitable new links to the frontier.
7. **Storage and indexer:** store or pass processed documents to the indexer, which builds searchable term-to-document postings.
8. **Revisit policy:** schedule previously fetched pages again when appropriate; update or remove obsolete index entries.

**Walk-through:** starting at an allowed department home page, the fetcher obtains HTML, the parser extracts a link to a course page, and the frontier schedules it. The indexer tokenizes the course page and adds its document ID to relevant postings. When the page changes, a later revisit updates the indexed content. The scheduling and duplicate checks prevent the crawler from blindly following the same links forever.

#### Harvest: a distributed crawler–indexer architecture

The textbook also discusses **Harvest**, a historical modular distributed architecture. Its [architecture diagram is on PDF page 48](../Books/ISR_Decode_Units03-06.pdf#page=48).

1. A **gatherer** collects documents from one or more servers and extracts resource descriptions or summaries from supported formats.
2. A **broker** receives those descriptions, builds an index and offers a query interface. A broker can combine information from multiple gatherers, and a gatherer can supply multiple brokers.
3. A **replicator** provides replicas to help handle demand; an **object cache** can reduce repeated transfers and access latency.
4. A user sends a query to the broker; the broker searches its index and returns relevant references. The user can then obtain the original object, potentially using the cache.

Example: a university gatherer summarizes public library pages and sends descriptions to an academic broker. A research broker may reuse the same descriptions instead of independently crawling everything. Compared with gathering full documents at one central site, this can distribute work and reduce transferred data, but summaries must be maintained and may omit information useful for a query. Harvest's gatherers and brokers are a particular historical design; modern crawlers need not use those names.

Use `robots.txt` guidance and published access policies, avoid overwhelming servers, and respect permissions and applicable terms. `robots.txt` is not an authentication mechanism or permission to access private data.

#### Crawling strategies

| Strategy | Idea | Trade-off |
|---|---|---|
| Breadth-first | Explore links level by level from seeds | Broad coverage but may spend effort on low-value areas |
| Depth-first | Follow a path deeply before backtracking | Can find deep pages but delay wider coverage |
| Focused | Prioritize pages and links relevant to a topic | Efficient for a domain, but relevance estimates can exclude useful paths |
| Priority / freshness-based | Rank URLs by importance or expected change | Useful under limited budget; estimates can be wrong |
| Incremental recrawl | Revisit existing pages according to change rate | Improves freshness within budget, not instant completeness |

#### Centralized versus distributed search architecture

| Aspect | Centralized | Distributed |
|---|---|---|
| Index/control | One logical index or coordinator | Multiple index shards or independently managed search sources |
| Scaling | Simpler management, but a logical bottleneck can emerge | Parallel indexing and queries; better capacity if balanced |
| Failure | A single point of failure unless replicated | Individual node failure can yield partial results; coordination and replicas needed |
| Ranking | Global statistics easier to maintain | Global scoring and merging require coordination |
| Cost | Less network coordination | More synchronization, network traffic and operational complexity |

A centralized logical index can still be physically distributed; distinguish an implementation's deployment from whether it searches independent collections.

**References:**
- [Decode ISR, unit 5, PDF page 47](../Books/ISR_Decode_Units03-06.pdf#page=47).
- [ISR Unit 5 study notes](../Study/unit-5-web-search.md).
- [Decode: Harvest diagram and components, pages 48–49](../Books/ISR_Decode_Units03-06.pdf#page=48).

## Q6(c) — Challenges in web searching

- **Scale and speed:** huge collections require distributed storage, indexing and low query latency.
- **Change and freshness:** pages appear, move, change or disappear; recrawling everything immediately is impractical.
- **Quality and spam:** duplicate pages, manipulation and misleading content degrade results.
- **Heterogeneity:** multiple languages, formats, scripts and media complicate parsing and relevance.
- **Ambiguity:** short queries such as `java` can mean a programming language, island or coffee.
- **Coverage:** authenticated, dynamically generated, blocked or unlinked resources may not be crawled; absence from the index is not proof that a page does not exist.
- **Privacy and fairness:** user data and ranking choices require careful handling.

**References:**
- [Decode ISR, unit 5, PDF page 41](../Books/ISR_Decode_Units03-06.pdf#page=41).
- [ISR Unit 5 study notes](../Study/unit-5-web-search.md).

## Q7(a) — Recommender systems and content-based recommendation

A **recommender system** ranks or suggests items likely to be useful to a user, based on the user's preferences, item features and/or patterns across users. Items can be documents, books, films, courses or products. Unlike a conventional search that starts with an explicit query, recommendation may proactively use a profile; real systems can combine both.

![Taxonomy of content-based, collaborative and hybrid recommenders](../../DL/Study/images/collaborative-filtering.jpg)

*Recommender system approaches by Moshanin, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Collaborative_Filtering_in_Recommender_Systems.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); unchanged.*


1. **Content analyzer:** extract document features such as words, TF–IDF vectors, topics, authors or subject tags.
2. **Profile learner:** build a user-interest profile from documents the user explicitly rated or implicitly interacted with; update it as preferences change.
3. **Filtering and ranking:** compare candidate document vectors with the profile, for example using cosine similarity.
4. **Presentation and feedback:** show the top items, explain matched features where useful, and incorporate feedback.

**Worked example:** features are `[security, retrieval]`. A user's normalized interest profile is proportional to `(2,1)`. Document A has `(1,0)`, document B `(0,1)`:

- `cos(user,A) = 2/√5 ≈ 0.894`.
- `cos(user,B) = 1/√5 ≈ 0.447`.

Document A ranks first under this simple model. A cold-start user has no reliable profile; new documents can be recommended if their content features exist. Excessive similarity can cause **overspecialization**: only familiar topics are shown.

**References:**
- [Decode ISR, unit 6, PDF page 71](../Books/ISR_Decode_Units03-06.pdf#page=71).
- [ISR Unit 6 study notes](../Study/unit-6-advanced-ir.md).

## Q7(b) — Vector space model for XML retrieval

In the **vector space model**, represent a document or XML element and the query as vectors of weighted terms. Term weights may combine term frequency and inverse document frequency (TF–IDF). Compare the vectors with cosine similarity and rank the larger scores first.

`cos(q,d) = (q · d) / (||q|| × ||d||)`.

To incorporate XML structure, dimensions can include a term and its field or path, such as `(title, retrieval)` or `(section/p, image)`. Alternatively, score text within selected elements and apply structural constraints separately. Specify which elements are indexed and how nested matches are deduplicated.

**Worked example:** use dimensions `(title:retrieval, paragraph:retrieval)` with `q = (1,1)`. Let element A be `(2,0)` and element B `(1,1)`:

- `cos(q,A) = 2/(√2 × 2) ≈ 0.707`.
- `cos(q,B) = 2/(√2 × √2) = 1`.

Under these illustrative weights, B ranks above A. In practice, weights and query intent matter: if the user specifically requests a title match, the system could restrict or weight the title field differently. A zero-length vector needs an explicit handling convention; cosine is otherwise undefined.

![XML document represented as a DOM tree of nested elements and text](../Study/images/xml-tree.png)

*DOM tree of an XML playlist by Steffen Staab, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:DOM-Tree-Example-For-WebScience-MOOC.png), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); unchanged. Element names and their indentation show parent–child relationships.*

**References:**
- [Decode ISR, unit 6, PDF page 64](../Books/ISR_Decode_Units03-06.pdf#page=64).
- [ISR Unit 6 study notes](../Study/unit-6-advanced-ir.md).
- [Technical: XML vector space model, page 98](../Books/ISR_Technical_Units03-06.pdf#page=98).

## Q8(a) — Content-based recommendation of documents

A **recommender system** ranks or suggests items likely to be useful to a user, based on the user's preferences, item features and/or patterns across users. Items can be documents, books, films, courses or products. Unlike a conventional search that starts with an explicit query, recommendation may proactively use a profile; real systems can combine both.

![Taxonomy of content-based, collaborative and hybrid recommenders](../../DL/Study/images/collaborative-filtering.jpg)

*Recommender system approaches by Moshanin, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Collaborative_Filtering_in_Recommender_Systems.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); unchanged.*


1. **Content analyzer:** extract document features such as words, TF–IDF vectors, topics, authors or subject tags.
2. **Profile learner:** build a user-interest profile from documents the user explicitly rated or implicitly interacted with; update it as preferences change.
3. **Filtering and ranking:** compare candidate document vectors with the profile, for example using cosine similarity.
4. **Presentation and feedback:** show the top items, explain matched features where useful, and incorporate feedback.

**Worked example:** features are `[security, retrieval]`. A user's normalized interest profile is proportional to `(2,1)`. Document A has `(1,0)`, document B `(0,1)`:

- `cos(user,A) = 2/√5 ≈ 0.894`.
- `cos(user,B) = 1/√5 ≈ 0.447`.

Document A ranks first under this simple model. A cold-start user has no reliable profile; new documents can be recommended if their content features exist. Excessive similarity can cause **overspecialization**: only familiar topics are shown.

**References:**
- [Decode ISR, unit 6, PDF page 71](../Books/ISR_Decode_Units03-06.pdf#page=71).
- [ISR Unit 6 study notes](../Study/unit-6-advanced-ir.md).

## Q8(b) — Collaborative versus content-based filtering

A **recommender system** ranks or suggests items likely to be useful to a user, based on the user's preferences, item features and/or patterns across users. Items can be documents, books, films, courses or products. Unlike a conventional search that starts with an explicit query, recommendation may proactively use a profile; real systems can combine both.

![Taxonomy of content-based, collaborative and hybrid recommenders](../../DL/Study/images/collaborative-filtering.jpg)

*Recommender system approaches by Moshanin, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Collaborative_Filtering_in_Recommender_Systems.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); unchanged.*


1. **Content analyzer:** extract document features such as words, TF–IDF vectors, topics, authors or subject tags.
2. **Profile learner:** build a user-interest profile from documents the user explicitly rated or implicitly interacted with; update it as preferences change.
3. **Filtering and ranking:** compare candidate document vectors with the profile, for example using cosine similarity.
4. **Presentation and feedback:** show the top items, explain matched features where useful, and incorporate feedback.

**Worked example:** features are `[security, retrieval]`. A user's normalized interest profile is proportional to `(2,1)`. Document A has `(1,0)`, document B `(0,1)`:

- `cos(user,A) = 2/√5 ≈ 0.894`.
- `cos(user,B) = 1/√5 ≈ 0.447`.

Document A ranks first under this simple model. A cold-start user has no reliable profile; new documents can be recommended if their content features exist. Excessive similarity can cause **overspecialization**: only familiar topics are shown.

Collaborative filtering predicts interests from user–item interactions. **User-based CF** finds users with similar rating patterns and recommends items they liked that the target user has not seen. **Item-based CF** finds items with similar interaction patterns and recommends items related to those the user liked. Model-based approaches such as matrix factorization learn user and item representations from the interaction matrix.

**Example:** A and B both liked documents X and Y. B also liked Z, which A has not read. A user-based recommender may suggest Z to A, subject to sufficient evidence. Common issues are sparse ratings, cold-start users/items, popularity bias and changing preferences.

For a user-based system, collect ratings or interactions, compute similarity over comparable items, select neighbors, aggregate their evidence for unseen items and rank the predictions. A simple illustrative rating matrix is:

| User | Document X | Document Y | Document Z |
|---|---:|---:|---:|
| A | 5 | 4 | Not rated |
| B | 5 | 4 | 5 |

Because A and B agree on X and Y, B's rating makes Z a candidate for A. This is a prediction, not a certainty; two shared ratings alone are weak evidence. Missing ratings mean **unknown**, not zero. An item-based variant instead compares columns and recommends items similar in interaction patterns to those A liked.

| Aspect | Content-based | Collaborative |
|---|---|---|
| Main evidence | Item features plus this user's profile | Interactions across users and items |
| Similarity | User profile versus item content | User–user, item–item or learned interaction patterns |
| New item | Can recommend if useful content features exist | Difficult with no interactions |
| New user | Difficult without preferences | Difficult without interactions |
| Diversity | Can over-specialize around known interests | Can discover items unlike previously liked content |
| Dependency | Good item descriptors | Sufficient, reasonably representative interactions |
| Explanation | “Matches your interest in retrieval” | “Users with similar interactions liked this” |

**Hybrid systems** combine the two kinds of evidence to mitigate some weaknesses. They do not automatically eliminate cold start or bias. Evaluate with a realistic temporal split and ranking measures such as precision@k or recall@k; protect user data and consider diversity, fairness and feedback loops.

**References:**
- [Decode ISR, unit 6, PDF page 69](../Books/ISR_Decode_Units03-06.pdf#page=69).
- [ISR Unit 6 study notes](../Study/unit-6-advanced-ir.md).
