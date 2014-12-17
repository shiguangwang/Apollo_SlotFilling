     TAC 2013 KBP Slot Filler Validation Evaluation Queries V1.1

                       September 5, 2013
       U.S. National Insitute of Standards and Technology


1. Overview

This package contains evaluation queries for the TAC KBP 2013 Slot
Filler Validation (SFV) track.  The input to the SFV track is a set of
candidate slot fillers returned by runs submittted to the TAC KBP 2013
English Slot Filling (SF) track; the system output for the SFV track
is a binary classification of each candidate slot filler in each SF
run.  

Please refer to the TAC KBP 2013 website
(http://www.nist.gov/tac/2013/KBP/) for further information.


2. Contents

  data/slot-filling_system_output

This directory contains 52 files, each of which represents a run
submitted in response to the TAC 2013 KBP English Regular Slot Filling
Evaluation Queries (LDC2013R14).  There were 18 English SF teams, and
each team submitted between 1 and 5 runs.  Each English SF team has an
identifier "SFV2013_XX" (XX ranging from 01 to 18), and its runs are
named "SFV2013_XX_Y" (Y ranging from 1 to 5).

The file SFV2013_XX_Y contains all of the non-NIL slot fillers
returned by run SFV2013_XX_Y.  Each line in the file consists of the
following tab-delimited fields:

   1. SF_query_id     -  slot filling query ID

   2. slot_name       -  slot name

   3. SFV_query_id    -  slot filler validation query ID

   4. docid 	      -  the ID of a document in the corpus that justifies 
      		         the relation between the SF query entity and the
      		         slot filler

   5. slot_filler     -  the (possibly normalized) slot filler

   6. filler_offsets  -  start-end offsets for the representative
                         mentions used to extract/normalize the
                         filler.

   7. entity_offsets  -  start-end offsets for the representative
                         mentions used to extract/normalize the
                         query entity.

   8. pred_offsets    -  start-end offsets for the text excerpts used
                         to justify the relation between the query
                         entity and the filler.

   9. conf_score      -  a confidence score for the response.

The file format is the same as the system output format given in the
TAC KBP 2013 English Slot Filling task description
(http://surdeanu.info/kbp2013/def.php), except that field 3 contains a
slot filler validation query ID rather than a SF run ID.  

The slot filler validation query ID (field 3) consists of the SF run
ID and filler-candidate-number.  For example "SFV2013_08_2_365" is the
365th candidate slot filler proposed by run "SFV2013_08_2", from the
team "SFV2013_08".

The output of a SFV run should be a single tab-delimited file with
exactly one judgment for each slot filler validation query ID.  The
possible judgments are:

     1: candidate slot filler is Correct or Redundant with reference KB
    -1: candidate slot filler is Wrong or Inexact

The definitions of Correct, Redundant, Wrong, and Inexact for slot
fillers are given in the TAC KBP 2013 English Slot Filling task
description (http://surdeanu.info/kbp2013/def.php).

In total, there are 52641 slot filler validation queries, though many
queries differ only in their slot filler validation query ID; this is
because different systems submitted by the same team, or that use the
same publicly available relation extraction package, often produce the
same candidate slot fillers.  The duplicate candidate slot fillers are
kept in order to preserve SF system provenance for each candidate slot
filler.


  data/SF2013SystemProfiles.txt

SF2013SystemProfiles.txt contains a description of each KBP 2013
English slot filling run, provided by the submitting team at the time
of submission; the names of software packages and resources in fields
11-26 have been standardized across teams.  The system profiles are
provided for SFV teams that wish to apply ensemble models or leverage
global (cross-system or cross-team) features, but the profiles are not
required for slot filler validation.

Each line of the system profiles file consists of 27 tab-delimited
fields; the first row is a header with the column labels. The column
descriptions are as follows:

   1. TeamID: SF team ID (e.g., SFV2013_08)	

   2. RunNumber: An integer (1-5)

   3. Web Use?: Did the run access the Web during the evaluation
   period ("Yes" or "No")

   4. 2009 Rank: The team's rank in KBP 2009 English Slot Filling
   (1-5, "below5", or "NA" if team did not participate in 2009)

   5. 2010 Rank: The team's rank in KBP 2010 English Slot Filling
   (1-5, "below5", or "NA" if team did not participate in 2010)

   6. 2011 Rank: The team's rank in KBP 2011 English Slot Filling
   (1-5, "below5", or "NA" if team did not participate in 2011)

   7. 2012 Rank: The team's rank in KBP 2012 English Slot Filling
   (1-5, "below5", or "NA" if team did not participate in 2012)

   8. Extract from KBP 2013 Source Corpus?: Did this run extract
   candidate slot fillers from the TAC KBP 2013 source documents
   ("Yes" or "No")

   9. Confidence Value has Meaning?: Did this run attempt to compute
   meaningful confidence values ("Yes" or "No")

   10. Confidence Value is a Probability?: Is the confidence value a
   probability? ("Yes" or "No")

   11. Query Expansion: Publicly available software packages used for
   query expansion ("InHouse" if using in-house software, "NA" if
   query expansion was not used or described)

   12. Document Retrieval: Publicly available software packages used
   for document retrieval ("InHouse" if using in-house software, "NA"
   if document retrieval was not used or described)

   13. Sentence Retrieval: Publicly available software packages used
   for sentence retrieval ("InHouse" if using in-house software, "NA"
   if sentence retrieval was not used or described)

   14. NER: Publicly available software packages used for named entity
   recognition ("InHouse" if using in-house software, "NA" if named
   entity recognition was not used or described)

   15. Nominal Tagging: Publicly available software packages used for
   nominal tagging ("InHouse" if using in-house software, "NA" if
   nominal tagging was not used or described)

   16. Coreference Resolution: Publicly available software packages
   used for coreference resolution ("InHouse" if using in-house
   software, "NA" if coreference resolution was not used or described)

   17. Third-party Relation/Event Extraction: Publicly available
   software packages used for relation/event extraction ("InHouse" if
   using in-house software, "NA" if third-party extractor was not
   used or described)

   18. Dependency Parsing: Publicly available software packages used
   for dependency parsing ("InHouse" if using in-house software, "NA"
   if dependency parsing was not used or described)

   19. POS Tagging: Publicly available software packages used for
   part-of-speech tagging ("InHouse" if using in-house software, "NA"
   if part-of-speech tagging was not used or described)

   20. Chunking: Publicly available software packages used for
   chunking ("InHouse" if using in-house software, "NA" if chunking
   was not used or described)

   21. Constituent Parsing: Publicly available software packages used
   for constituency parsing ("InHouse" if using in-house software,
   "NA" if constituency parsing was not used or described)

   22. Main Slot-filling Algorithm: Main approach to extracting slot
   fillers ("NA" if main approach was not described)

   23. Learning Approach: Learning approach used ("NA" if no learning
   approach was used or described)

   24. Learning Algorithm: Specific learning algorithm used ("NA" if no learning
   algorithm was used or described)

   25. Ensemble Model: Ensemble model used on top of learning
   algorithm above ("NA" if no ensemble models were used or described)

   26. External Resources: External data resources used

   27. Other salient features: Other salient features of the run,
   including what distinguishes this run from other runs submitted by
   the same team


  ./README.txt

This file.


3. Contact Information

For further information about this data release, or the TAC 2013 KBP
project, contact:
   tac-manager@nist.gov

-----------------------------------------------------------------------------
README created by Hoa Dang (hoa.dang@nist.gov) on September 4, 2013
README updated by Hoa Dang (hoa.dang@nist.gov) on September 5, 2013
