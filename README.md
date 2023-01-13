# 🌱 Project Language 

This repository is the central point for documentation and data for your project. You will find several folders where you can store the data and code used as you create data and train models for a new language. 

`0_original_texts`: This folder contains the original text files for the project. This is a record of the original state of the texts before any pre-processing and annotation.

`1_lookups_data`: This folder contains the json lookups files for unambiguous lemmata, pos, and feats. This data is used to document the bulk annotation process and is superseded by the manually annotated data from INCEpTION.

`2_new_language_object`: This folder contains the nlp object folder from either Cadet or the Cadet notebook. This folder is fetched during training to load the new language object.

`3_inception_export`: This folder contains the CoNLL-U data that is exported from INCEpTION once annotation work is completed. If versioning of exports is required, you can place each version is its own subfolder. During training, this folder provides the main source of training data and should be split between training and validation sets.

`4_trained_models`: This folder contains packaged models and model cards for your new language models.

## Dataset Summary 
- Central Margins in Digital Japanese History is a Kanbun-based project focusing on the analysis of the Dai Nihon shi (大日本史　The History of Great Japan, 1657-1906), one of the most monumental historiographical works ever produced in Japan through annotation and model training. In particular, the project is concerned with the study of commentaries ("footnotes") included in the text, in which the authors of the Dai Nihonshi indicated the historical sources that they had referenced and thus arguably considered reliable. Since the compilation of the Dai Nihon shi took ca. 250 years, the source provides a useful starting point to analyze potential changes in the historical consciousness of the compilers.

## Language(s) 
- Kanbun (literary Sinitic)

## Curation Rationale
- The Dai Nihon shi in its current form consists of 397 + 5 scrolls, written in Kanbun for the most part with some poems embedded in it in classical Japanese. The high proportion of character variations and the presence of reading aids* render the OCR process exceedingly difficult and require significant manual corrections. The machine-readable portion of the source above originates from an openly accessible platform dedicated to making premodern Japanese historical works available (http://miko.org/~uraki/kuon/furu/text/dainihonsi/dainihon.htm). The corpus contains ca. 40% of the text (from different sections of the Dai Nihon shi). The rest of the text has been manually annotated and the titles of the reference works used by the authors of the Dai Nihon shi have been collected by hand by Horvath. The digitially processed version of this data collection will soon be connected with the annotated (and machine-readable) parts of the corpus.
* Reading aids refer to small characters that appear next to the main body of the text and help the reader reorder the Chinese characters that the text consists of according to the grammatical structures of the Japanese language. From an OCR perspective, the problem here is that these "reading aids" are often treated by the OCT software as integral parts of the text, creating a confusing output. The source of the machine-readable version of the Dai Nihon shi does not contain reading aids for the most part.
 
## Source Data
- The nature and characteristics of the dataset has been described above. In terms of the research process, The text files have been saved in smaller segments to facilitate the processing of the content - the files names refer to scroll numbers and number of the text segments in the case of longer scrolls. The files have been processed through a colab-based platform (created by Budak) to prepare them for annotation in INCEpTION. Horváth also experimented with annotating the texts in CATMA, but the files uploaded here have been all annotated in INCEpTION. Horváth annotated ca. 70 000 lines with a primary focus on named entities (WORK_OF_ART, LOC, PER). INCEpTION by default allowed the annotation of work titles as OTH (other), therefore these tags have been converted to WORK_OF_ART subsequently. The model, trained to recognize work titles, has been created achieving ca. 90% of accuracy. Eventually, the entire available corpus has been annotated which can be an effective basis for NER-based inquiries, particularly once the entire Dai Nihon shi becomes available in a machine-readable format. 

## Personal and Sensitive Information, Potential for Human Harm 
- The dataset is based on an early modern text and reflects the historical beliefs of the Mito School, a scholarly group in Japan. The text contains very limited personal information which makes even the question of authorship difficult to determine since the list of authors is not provided in the work. (One needs to do further research to retrieve information about the identity of the contributors over the 250 years of the compilation process.) The Dai Nihon shi was initiated by Tokugawa Mitsukuni (1627-1700), the second daimyo (feudal lord) of the Mito domain and a grandson of Tokugawa Ieyasu, the founder of the Tokugawa Shogunate. According to the available primary sources, Mitsukuni aimed to critically document the history of Japan through multiple perspectives into account (by hiring scholars of diverse backgrounds), but the final content stops in the medieval period.

## Licensing Information
- The Dai Nihon shi itself is not under copyright, but reusing the code and the annotated files requires permission.

## Dataset Curators
- Alíz Horváth (PI), Eötvös Loránd University
with Nick Budak (Stanford University) and Andy Janco (University of Pennsylvania)

## Citation Information
- Horváth, Alíz, Nick Budak, Andy Janco. 2022. Central Margins in Digital Japanese History. New Language for NLP: Building Linguistic Diversity in the Digital Humanities Institute / Kanbun.  
