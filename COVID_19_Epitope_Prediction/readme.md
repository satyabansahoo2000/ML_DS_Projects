## Introduction

Due to spread of COVID-19, vaccine development is beingdemanded as soon as possible. Despite the importance of data analysis in vaccine development, there are not many simple data sets that data analysts can handle. We published the dataset and the sample code for Bcell epitope prediction, one of the key research topics in vaccine development, available for free. This dataset was developed during our research process and the data contained in it was obtained from [IEDB](https://www.iedb.org/) and [UniProt](https://www.uniprot.org/). We would like to express our deepest gratitude to everyone who helped us. We briefly describe the B-cell epitope predictions covered by this dataset.  For details, please refer to [our paper](https://www.biorxiv.org/content/10.1101/2020.07.27.224121v1), [our blog (only in Japanese)](https://future-architect.github.io/articles/20200801/), and others. B-cells inducing antigen-specific immune responses in vivo produce large amounts of antigen-specific antibodies by recognizing the subregions (epitope regions) of antigen proteins. They can inhibit their functioning by binding antibodies to antigen proteins. Predicting of epitope regions is beneficial for the design and development of vaccines aimed to induce antigen-specific antibody production. We believe that this dataset and code will be widely useful not only for COVID-19 but also for future medical data analysis.

**The data:** Information on whether or not an amino acid peptide exhibited antibody-inducing activity (marked by an activity label) could be obtained from IEDB, which was used in many previous studies. Accordingly, this information was used as the label data. We also obtained the epitope candidate amino acid sequences (peptides) and the activity label data from the B-cell epitope data provided in IEDB. The presented antibody proteins were restricted to IgG that constituted the most recorded type in IEDB. For convenience, we excluded records representing different quantitative measures of antibody activity for the same peptide from experiments. The epitope data obtained from IEDB corresponded to the five types of activity: "Positive-High," "Positive-Intermediate," "Positive-Low," "Positive," and "Negative." However, due to the limited number of data elements marked with the "Positive-High," "Positive-Intermediate," and "Positive-Low" labels, we equally considered these labels as "Positive", thereby attributing the task to a binary estimation.
Content

This contains three data files:

    input_bcell.csv : this is our main training data. The number of rows is 14387 for all combinations of 14362 peptides and 757 proteins.
    input_sars.csv : this is also our main training data. The number of rows is 520.
    input_covid.csv : this is our target data. there is no label data in columns.

All of three datasets consists of information of protein and peptide:

    parent_protein_id : parent protein ID
    protein_seq : parent protein sequence
    start_position : start position of peptide
    end_position : end position of peptide
    peptide_seq : peptide sequence
    chou_fasman : peptide feature, $\beta$ turn
    emini : peptide feature, relative surface accessibility
    kolaskar_tongaonkar : peptide feature, antigenicity
    parker : peptide feature, hydrophobicity
    isoelectric_point : protein feature
    aromacity: protein feature
    hydrophobicity : protein feature
    stability : protein feature

and bcell and sars dataset have antibody valence(target value):

    target : antibody valence (target value)

## Relevant Papers

[Epitope Prediction of Antigen Protein using Attention-Based LSTM Network (2020, bioRxiv)](https://www.biorxiv.org/content/10.1101/2020.07.27.224121v1)

## Acknowledgements

Data is provided from [The Immune Epitope Database(IEDB)](https://www.iedb.org/) and [UniProt](https://www.uniprot.org/).

## Inspiration

Automated methods for B-cell epitope prediction.Machine learning helps rapid vaccine development.

## Disclaimer

We make no warranties regarding the correctness of the data, and disclaim liability for damages resulting from its use. We cannot provide unrestricted permission regarding the use of the data, as some data may be covered by patents or other rights.
