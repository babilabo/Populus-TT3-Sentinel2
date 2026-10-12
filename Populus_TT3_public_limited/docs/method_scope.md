# Interpretation notes

- The initial stratified random pixel-sample evaluation and the added fixed spatial-block evaluation are different protocols; their numbers must not be combined as though they were one test.
- The three seeds in the added experiments represent repeated training on **one fixed spatial partition**, not three spatially independent holdouts.
- Spatial-block source-domain results do not establish classification accuracy in Kuqa City.
- Kuqa mapped area is a **source-model predicted candidate area**, not independent ground-truth species extent.
- Softmax scores and uncertainty measures are descriptive outputs and do not establish target-domain reliability.
- The historical GEE scene inventory available for an October 10 cutoff is not published here as an inventory for the confirmed October 20 autumn window.
- The per-class CSV gives seed-42 source-domain spatial-block metrics, not the six-class confusion-count matrix of the original random split.
