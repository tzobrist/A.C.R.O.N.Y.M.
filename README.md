# A.C.R.O.N.Y.M.
ChatGPT-enhanced Technical Paper Acronym Generator Tool

#### Purpose:
Everyone loves clean acronym titles for their research papers. This tools allows you to use an already existing GPT API key and some under-the-hood NLP/prompt engineering to generate relevant acronyms for your paper.
The tool accepts your paper's abstract (or any type of generalized overview text) as input and outputs a user-specified number of acronyms and their associated titles.

#### What does A.C.R.O.N.Y.M. stand for?
ACRONYM stands for <b><i>A</i></b>utonomous <b><i>C</i></b>ontext-aware <b><i>R</i></b>efactoring <b><i>O</i></b>f the <b><i>N</i></b>ame for <b><i>Y</i></b>our <b><i>M</i></b>aterial. It is only fitting that for a project of this nature it has a clever acronym as a title.
> I came up with this name in the middle of the development process so no, the tool didn't generate it.

#### Usage:
I feel like the usage is pretty straight forward. Each field has tooltips referencing what they are responsible for and can be filled out with the user's desired setup.

![image](https://github.com/tzobrist/A.C.R.O.N.Y.M./assets/77289395/df410628-763d-4941-9378-34df1ae6afc3)

- API Key: User's GPT API Key to access GPT models
- GPT Model: Model to use for query
- Prompt Size: Max number of tokens to use within query (1300 is usually enough)
- Number of Acronyms: # of acronyms to generate based off of input text
- Abstract: Your paper's abstract to use as source material
- A.C.R.O.N.Y.M. Output: Where generated acronyms will end up
> [!NOTE]
> ACRONYM doesn't handle numbered lists well (i.e. 1) Item 1, 2) Item 2, 3) Item 3...) so preprocessing the abstract to remove those may yield more beneficial results.

#### Example Query:
Paper Abstract / Input:
"Financial services generate a huge volume of data that is extremely complex and varied. These datasets are often stored in silos within organizations for various reasons, including but not limited to regulatory requirements and business needs. As a result, data sharing within different lines of business as well as outside of the organization (e.g. to the research community) is severely limited. It is therefore critical to investigate methods for synthesizing financial datasets that follow the same properties of the real data while respecting the need for privacy of the parties involved. This introductory paper aims to highlight the growing need for effective synthetic data generation in the financial domain. We highlight three main areas of focus that are of particular importance while generating synthetic financial datasets: Generating realistic synthetic datasets, measuring the similarities between real and generated datasets, ensuring the generative process satisfies any privacy constraints. Although these challenges are also present in other domains, the additional regulatory and privacy requirements within financial services present unique questions that are not asked elsewhere. Due to the size and influence of the financial services industry, answering these questions has the potential for a great and lasting impact. Finally, we aim to develop a shared vocabulary and context for generating synthetic financial data using two types of financial datasets as examples."
> Taken from Samuel A. Assefa, Danial Dervovic, Mahmoud Mahfouz, Robert E. Tillman, Prashant Reddy, and Manuela Veloso. 2021. Generating synthetic data in finance: opportunities, challenges and pitfalls. In Proceedings of the First ACM International Conference on AI in Finance (ICAIF '20). Association for Computing Machinery, New York, NY, USA, Article 44, 1–8. https://doi.org/10.1145/3383455.3422554

ACRONYM Output:
1. FINDER: Financial INformation Data Extraction and geneRation
2. RAPID: Realistic Assessment and Privacy-preserving data synthesIs for financial Datasets
3. SHIELD: Synthesizing High-quality, Independent, and Efficiently Labeled data for financial Datasets
4. GENESIS: Generating Efficient and Naturalistic synthEtic financial dataSets with Integrity and Similarity
5. SPARK: Synthesizing Pseudonymized and Accurate financial datasets to Release Knowledge
6. SAFEGUARD: Synthetically Acquiring Financial data while Excelling in ensuring privacy and Generating Uniquely Authentic datasets foR business Decision-making
7. ECHO: Evaluating the Compatibility between real and syntHetic financial datasets for analysis and privacy protectiOn
8. RESOLVE: Regulatory and Enhanced Synthetic data generation for Optimized data in the financiaL Volumetric Environments
9. ASCENT: Assessing Similarities and Constraints of financial datasets for Enhanced Natural data Transformations
10. PRAISE: Privacy-preserving Realistic Assessment of financial data Incorporating Synthetic data for Evaluation
> Some of these are stretches as far as acronym/title combos, this issue is highlighted in the future work and will continue to be refined.
> But if I were to rename this paper it could be something like "GENESIS Framework: Generating Efficient and Naturalistic synthEtic financial dataSets with Integrity and Similarity" since the paper proposes a shared context (framework) between synthetic finanical datasets to better satisfy the current need.

#### Future Work:
1. Refine prompt to allow for more obscure word usage and reduce chance of invalid titles
2. Refine synonym supplementation
3. Reformat output so titles are correctly capitalized
4. UI beautification (I didn't spend a lot of time on it, more so the backend)
