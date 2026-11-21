# Deep Learning: endsem study guide

BE IT, Semester VII, 2019 pattern, subject 414443. This guide groups the seven retained 70-mark papers by concept, then adds related book material. Answers are original summaries; embedded images are credited and licensed individually.

## Start here

| Unit | Notes | Main question clusters |
|---|---|---|
| 3 | [Recurrent neural networks](unit-3-rnn.md) | RNN types, feed-forward vs recurrent, LSTM, encoder-decoder, recursive networks |
| 4 | [Autoencoders](unit-4-autoencoders.md) | Architecture, bottleneck, undercomplete, sparse, denoising, contractive, stochastic, applications |
| 5 | [Representation learning](unit-5-representation.md) | Representations, greedy pretraining, transfer learning, domain adaptation, CNN variants and DenseNet |
| 6 | [Applications](unit-6-applications.md) | Image classification, social networks, speech recognition, recommender systems and NLP |

The papers generally offer **Q1 or Q2**, **Q3 or Q4**, **Q5 or Q6**, and **Q7 or Q8**. Those pairs broadly correspond to Units 3, 4, 5 and 6 respectively, but a question can cross units. Verify the instructions on your actual exam.

## Papers analyzed

The links below point to the repository copies. They are currently Git LFS pointers in this checkout; install Git LFS and hydrate them to open the PDFs. The content was checked against hash-verified copies during preparation.

| Short name used in notes | Paper |
|---|---|
| N22 | [Nov-Dec 2022](../PYQ/DL_Endsem_2022_Nov-Dec.pdf) |
| M23 | [May-Jun 2023, backlog](../PYQ/DL_Endsem_2023_May-Jun_Backlog.pdf) |
| N23 | [Nov-Dec 2023](../PYQ/DL_Endsem_2023_Nov-Dec.pdf) |
| M24 | [May-Jun 2024, backlog](../PYQ/DL_Endsem_2024_May-Jun_Backlog.pdf) |
| M25 | [May-Jun 2025](../PYQ/DL_Endsem_2025_May-Jun.pdf) |
| N25 | [Nov-Dec 2025](../PYQ/DL_Endsem_2025_Nov-Dec.pdf) |
| M26 | [May-Jun 2026](../PYQ/DL_Endsem_2026_May-Jun.pdf) |

**Counting caveat:** the removed Nov-Dec 2024 DL paper and retained M26 paper have the same questions but different paper codes. They are treated as one question set, not independent evidence of topic frequency.

## Question-to-topic map

These are paraphrased prompts, not transcriptions. Each semicolon separates subquestions. Unit links above contain the associated explanations and diagrams. Questions that cross units are listed in the unit that best explains them.

| Paper | Q1 / Q2 | Q3 / Q4 | Q5 / Q6 | Q7 / Q8 |
|---|---|---|---|---|
| N22 | Feed-forward vs RNN and RNN types; seq2seq / LSTM; RNN types | Unsupervised autoencoders; contractive / applications and retrieval; denoising | Greedy pretraining; representation learning / distributed representation; domain adaptation vs transfer | Graph convolution and RNN for NLP; CNN image classification / recommendation types; speech and bidirectional RNN |
| M23 | RNN vs recursive; LSTM / seq2seq; recursive types and advantages | Sparse architecture; applications / regularization and sparsity; architecture and hyperparameters | Transfer; DenseNet / greedy pretraining; representation and distributed representation | CNN/RNN for NLP; deep recommenders / social network analysis; CNN image classification |
| N23 | Feed-forward vs RNN; RNN types / LSTM; encoder-decoder and recursive networks | Autoencoder applications; denoising and contractive / sparse; undercomplete | Greedy pretraining; DenseNet / CNN variants; transfer and domain adaptation | Speech recognition; recommenders / image classification techniques; NLP |
| M24 | LSTM; seq2seq / feed-forward vs RNN and types; LSTM components and advantages | Undercomplete vs sparse; denoising / architecture and applications; bottleneck | Greedy pretraining; transfer / vanishing gradients; distributed representation | Traditional vs deep speech recognition; recommendation types / graph terminology and centrality; image classification |
| M25 | RNN types and applications; RNN vs feed-forward / recursive networks; LSTM | Encoder and undercomplete; regularized autoencoder / stochastic encoders and decoders; denoising vs contractive | DenseNet; domain adaptation / transfer; greedy pretraining | Deep recommenders; NLP framework / CNN image classifier; social network analysis |
| N25 | Sequence modeling and applications; RNN vs simple network / hierarchical modeling with recursive networks; RvNN vs RNN vs feed-forward | Encoder-decoder pattern; regularized autoencoder / applications; contractive vs stochastic | CNN variants; domain adaptation / distributed representation; greedy pretraining | NLP; deep recommenders / CNNs in vision; deep learning for social network analysis |
| M26 | RNN and four arrangements; variable length and memory / vanishing gradients and LSTM; recursive vs recurrent | Encoder and decoder; autoencoder vs PCA/clustering; training hyperparameters / denoising; contractive; undercomplete vs sparse | DenseNet; transfer in CNN; domain adaptation types / representation challenges; DenseNet for classification; transfer framework | Recommendation types; CNN classification / NLP applications and RNN vs CNN; centrality |

## How to use

1. Study the topic explanation and redraw its diagram without looking.
2. Answer the listed PYQ variants in your own words, including all parts of the question.
3. Use the book links for deeper reading and original illustrations. `#page=` refers to the **PDF viewer page**, not the printed book page. If your viewer ignores the fragment, enter the page manually.
4. For an 8–9 mark answer, aim for a definition, labelled diagram, working or steps, an example, and advantages/limitations as appropriate. For a comparison, use a table. Marks are not a guarantee of how many points the examiner expects.
5. Prioritize recurring themes, but do not assume past questions predict the next paper.

Images are saved locally for offline viewing in Markdown preview. Some come from Daniel Voigt Godoy's openly licensed book illustrations; others come from Wikimedia Commons or an open-access paper. Captions include sources and licenses. Links to figures in the repository's books open the relevant PDF pages rather than reproducing those figures.

**Sources:** [DL reference, units 3–6](../Books/DL_Reference_Units03-06.pdf), [technical book](../Books/DL_Technical_Units03-06.pdf), [Decode book](../Books/DL_Decode_Units03-06.pdf), and the two labelled RNN supplements in [Books](../Books). The supplements use another syllabus's printed numbering and are supporting reading, not the current unit map.
