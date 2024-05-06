## <div align="center"> General Description of Thyroid Disease Databases <br> and Related Files </div>

### Overview

This directory contains 6 databases, corresponding test set, and <br>
corresponding documentation.  They were left at the University of<br>
California at Irvine by Ross Quinlan during his visit in 1987 for<br>
the 1987 Machine Learning Workshop.  <br>

### Documentation

The documentation files (with file extension "names") are formatted to<br>
be read by Quinlan's C4 decision tree program.  Though briefer than<br>
the other documentation files found in this database repository, they<br>
should suffice to describe the database, specifically:<br>

  - Source
  - Number and names of attributes (including class names)
  - Types of values that each attribute takes

In general, these databases are quite similar and can be characterized
somewhat as follows:
   
  - Many attributes (29 or so, mostly the same set over all the databases)
  - Mostly numeric or Boolean valued attributes
  - Thyroid disease domains (records provided by the Garavan Institute<br>
    of Sydney, Australia)
  - Several missing attribute values (signified by "?")
  - Small number of classes (under 10, changes with each database)
  - 2800 instances in each data set
  - 972 instances in each test set (It seems that the test sets' instances<br>
    are disjoint with respect to the corresponding data sets, but this has<br>
    not been verified)

### Relevant Work
   
See the following for a discussion of relevant experiments and related work:

  * Quinlan,J.R., Compton,P.J., Horn,K.A., & Lazurus,L. (1986).<br> Inductive knowledge acquisition: A case study.<br> In Proceedings of the Second Australian Conference on Applications<br> of Expert Systems. Sydney, Australia.
  * Quinlan,J.R. (1986). Induction of decision trees. Machine Learning,<br> 1, 81--106.

### Note

**Note that the instances in these databases are followed by a vertical<br>
bar and a number.  These appear to be a patient id number.  The vertical<br>
bar is interepreted by Quinlan's algorithms as "ignore the remainder of<br>
this line".** <br>

## Additional Data Files

This database now also contains an additional two data files, named 
`hypothyroid.data` and `sick-euthyroid.data`.  They have approximately the
same data format and set of attributes as the other 6 databases, but
their integrity is questionable.  Ross Quinlan is concerned that they
may have been corrupted since they first arrived at UCI, but we have not
yet established the validity of this possibility.  These 2 databases differ
in terms of their number of instances (3163) and lack of corresponding 
test files.  They each have 2 concepts (negative/hypothyroid and 
sick-euthyroid/negative respectively).  Their source also appears to
be the *Garavan institute*.  Each contains several missing values.<br>

### Latest Addition

Another relatively recent file `thyroid0387`.data has been added that 
contains the latest version of an archive of thyroid diagnoses obtained 
from the *Garvan Institute*, consisting of ****9172 records from 1984 to early 1987****.<br>

### Domain Theory

A domain theory related to thyroid desease has also been added recently 
`(thyroid.theory)`.

### Donation

The files `new-thyroid.[names,data]` were donated by Stefan Aberhard.
