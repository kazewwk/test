of the designed system. In the next three sections, we give an overview of the sources of quantitative information that are useful to identify model parameters.

## 6.6.1 Datasets from the biological literature

Parameter values are typically inferred from measured experimental data (see Section 6.6.3 ‘Parameter Inference and Model Selection’). Sometimes parameter values can also be derived from biophysical values and computations using insight into the biological processes involved. Most often, the first step when looking for particular parameter values consists of searching the specialised literature and sifting through a large amount of papers to extract the relevant information. This, however, can be quite time-consuming and inefficient. This is why scientists and researchers have started gathering and curating this information in order to deposit it in freely accessible, online repositories. One such popular repository recently developed at the Systems Biology Department in Harvard (USA) and the Weizmann Institute (Israel) is called BioNumbers (http://bionumbers.hms.harvard.edu/). The BioNumbers website provides access to a growing number of biological and biophysical values extracted from the literature, together with the source used to provide the values. The centralisation of this information greatly facilitates the search for biologically relevant values, which can be useful for estimating the values of parameters appearing in biological models.

## 6.6.2 Datasheets from the characterisation of synthetic biology parts

Another way of obtaining useful information for the design of models and the identification of their parameters comes from the direct and methodical wet laboratory characterisation of engineered synthetic biology parts. Electronic engineers use TTL Data Books listing standard electronic components and their characteristics in order to choose the components required to construct their circuits. In a similar way, the ultimate goal of standardisation and characterisation of synthetic biology parts is to provide synthetic biologists with a catalogue of standard parts together with their associated characterisation datasheets. To be useful, these datasheets should contain enough quantitative information to allow a synthetic biologist to appropriately choose the specific parts that will yield the desired behaviour for an engineered system. An example of ‘gold standard’ datasheet is the BBa\_F2620 part datasheet giving quantitative characterisation information of a genetic receiver device (see http://parts.igem.org/wiki/images/f/fe/EndyFig1-F2620DataSheet.pdf). This receiver device takes the concentration of an inducer molecule as input and produces a specific output signal in response. The corresponding datasheet defines a number of aspects of the behaviour of the device: the strength of the output signal at different inducer concentrations, the time evolution of the output, the reliability or expected time to failure of the device, the degree of compatibility with other inducers and an indication of the type and amount of cellular resources the device consumes. Significantly, the authors of this datasheet underline the importance of measuring a large number of properties in order to comprehensively characterise genetic elements, especially those that describe the way the parts interact with the chassis in which they are intended to function. This hints at the necessity of producing high-quality datasheets of well-characterised parts in order to support the rapid and efficient reuse of the engineered parts or devices in various systems of increasing complexity. The creation of a registry of professionally characterised biological parts is one of the main goals of BIOFAB (see Chapter 3). These characterisation data are very useful to build mathematical models of the characterised parts and to identify their parameters.

## 6.6.3 Parameter inference and model selection

Given experimental data of sufficient quality and quantity it is possible to estimate the values of parameters appearing in mathematical models (this is called parameter inference or parameter estimation) and to decide which model is ‘better’ at explaining a given process (this is called model selection).

Typically, wet laboratory experimental data consist of time course measurements of the model species under some in vivo or in vitro conditions, such as time series measurements of protein concentrations under specific experimental conditions. Given these experimental data, parameter inference can be posed as a parameter optimisation problem where the function to be optimised takes as inputs the experimental data and the model with the chosen parameter values and gives as output a measure of how well simulations/predictions of the model with these particular parameter values match the experimental data. The optimal parameter estimates are those that maximise the objective function.

Model selection, on the other hand, refers to the task of selecting the ‘most appropriate models within a set of competing candidate models. Generally, models with more parameters fit the data better than models with fewer parameters and this must be accounted for. This is typically done using a parsimony principle so that given two competing models which explain the data equally well, the simpler one will be preferred. This is done using concepts such as the Likelihood Ratio Test (LRT), the Akaike Information Criterion (AIC) or the Bayesian Information Criterion (BIC).

## 6.7 Information Provided by Synthetic Biology Models

## 6.7.1 Metrics of interest in synthetic biology

From an engineering design point of view, the purpose of mathematical models in synthetic biology is to enable fast, efficient and reliable prediction and pre-assessment of the behaviour, robustness and performance of a designed system before its actual wet laboratory implementation. In particular, based on a mathematical model several metrics of interest to the designer (see Fig. 6.5) can be estimated in silico for the envisioned design(s). These metrics can be, for example, the time it takes for the system to respond to a step change at its input, the expected steady-state amplitude of the output of the system, the tunability of the output with respect to some of the parameters of the model or the robustness of the system to environmental perturbations. All of these metrics are extremely important in the appropriate design of a synthetic biology system. Estimating them in silico based on constructed models can be done efficiently through mathematical analysis and numerical simulations of the models.

![](images/page_114_chart_2.jpg)

<details>
<summary>line</summary>

| Parameter | Description |
| --- | --- |
| d | Desired final value (Initial value) |
| d + \(\epsilon\) | Output level (Overhoot point) |
| d - \(\epsilon\) | Output level (Stable state) |
| Static error | Vertical distance from peak to end of oscillation |
| Rise time | Time interval where the output exceeds the threshold |
| Settling time | Time interval where the output approaches the threshold |
</details>

Fig. 6.5 Example of typical performance metrics for the time evolution of the output of a designed system.

## 6.7.2 Model-based numerical simulations

To ensure that the in silico designed systems behave as desired, the proposed designs and their corresponding models are numerically simulated in various situations. This step is useful to check that models are characterised by behaviours and performances coherent with the initial design specifications. During this step the various metrics of interests are estimated in silico (Fig. 6.5). If the behaviour or performance are not satisfactory then some additional in silico iterations will be necessary to refine the designs/models until they are deemed acceptable.

## 6.7.3 Fundamental limits on system operation

Mathematical analysis of a model provides the designer with important information regarding the possible types of behaviours that can be expected from the implementation of a model, and also the fundamental limits of the designs, as well as ways to improve the design.

## 6.7.3.1 Identifying important controlling factors and weak spots in the design analysis of the models

Once models have been created and their parameters determined, these models can be mathematically analysed in order to characterise their qualitative behaviour and identify important controlling factors and ways to improve the design. Which parameters have the ‘largest impact’ on the model behaviour? This is typically discovered through what is called a parameter sensitivity analysis as explained in more detail below. What types of behaviours can be expected from the considered model and how can this behaviour change when the parameter values are modified? This is done through bifurcation analysis (see below). How robust is the behaviour/performance of the designed model to structural and dynamic perturbations?

## 6.7.3.1.1 Parameter sensitivity analysis

The goal of a parameter sensitivity analysis is to determine the influence of each parameter or combination of parameters on the behaviour or performance of the model. Sensitive parameters are those which are primarily responsible for significant changes in dynamical behaviour or performance and their value should be chosen wisely. Local sensitivity analysis is the study of the changes in the model output or performance function with respect to small perturbations in individual specified parameter values. Global sensitivity analysis enables an examination of the response of the system output or performance to simultaneous variations in parameter values across the whole admissible range of parameter variations. Global sensitivity analysis is of particular importance in biological models for which parameters can vary within large intervals depending on their meaning.

Examples of sensitivity analysis software tools developed specifically for biological systems include BioSens (http://thedoylegroup.org/research/biosens/), SensSB (Rodriguez-Fernandez and Banga, 2010) and SBML-SAT (Zi, Zheng et al., 2008).

## 6.7.3.1.2 Bifurcation analysis

This type of analysis informs the designer about transitions in dynamical regime induced by variations in parameter values. In particular, bifurcation analysis allows one to characterise regions in the parameter space in which the steady-state behaviour of the system remains qualitatively the same. At the boundaries of such regions, a qualitative change in the steady-state behaviour occurs, e.g. increasing the value of a single parameter while keeping the others constant leads to a transition from a unique asymptotically stable equilibrium point to an asymptotically stable periodic oscillation. The characterisation of these regions provides crucial information for the design as it allows the identification of the parameter regions/ranges within which a desired behaviour can be obtained. Numerical continuation analysis tools such as XPPAUT (Ermentrout et al., 2003) or MATCONT (Dhooge et al., 2003) can be used to perform a bifurcation analysis of a given model once an initial guess for its associated steady-state solution is known.

## 6.7.3.1.3 Robustness analysis

Although several designs can lead to the same behaviour, their respective ability to withstand perturbations may be very different. Provided that enough information is known about the perturbation (at least an upper bound on the energy of the perturbation), robust analysi of the models allows the assessment of their relative immunity to such perturbations. In particular, this step can prove very informative for the robust design of systems, and established multivariable robust control techniques can be used to that effect in the design process.

A widely used tool for this type of analysis is the Matlab Robust Control Toolbox (http://www.mathworks.com/products/robust/). The SBML-SAT tool mentioned above also implements algorithms for robustness analysis, as does the BIOCHAM (Rizk, Batt et al., 2009) modelling environment.

## 6.7.3.2 Determining constraints/limits on system behaviour/performance through mathematical analysis

By mathematically analysing a model or a family of models, some information can be gained regarding the conditions required to obtain a particular behaviour or ways to improve the design but also, and most importantly, regarding the fundamental limits that constrain the considered design — for example, by using a combination of control and information theory to mathematically obtain a fundamental limit on the maximum suppression of molecular fluctuations that can be obtained using any type of feedback control mechanism (Lestas, Vinnicombe, et al., 2010). The result shows that the limit is inversely proportional to the quartic root of the number of signalling events, making it extremely expensive to increase accuracy (e.g. to reduce molecular fluctuations by one order of magnitude you need to increase the number of signalling events by four orders of magnitude). This type of result is very useful for the design of synthetic biology systems since it informs the designer about what can be expected at best from any design and thus allows one to define the limits of what is achievable by a particular design.

## 6.8 Computational Tools for In Vivo or In Vitro Implementation of Synthetic Biology Systems

Once mathematical analysis and numerical simulations indicate that the models satisfy the design specifications, the synthetic biologist can focus his or her attention on the laboratory realisation of the proposed designs. This initiates the construction, characterisation and testing phase of the engineering design cycle (Fig. 6.1).

The laboratory implementation requires translation of the candidate synthetic biology design(s) into a biological language that the host cell can understand and ‘execute’. This typically means converting the design into an appropriate DNA sequence that the cell transcription/translation machinery can use to implement the desired synthetic biology circuit.

If the design is based on the interconnection of standard, well-characterised parts for which the associated models and parameter values are known then the implementation can be quite straightforward. In this situation, the physical design requires the assembly of the DNA sequences associated with the different parts into a larger section of DNA that implements the design (see Chapter 3). The assembly phase also requires the integration of this larger piece of DNA into plasmid vectors or into the chromosome of the host cell. The assembly phase can range in scale from assembling a gene optimised to efficiently express a protein with a given amino acid sequence, to assembling a set of genes to form a pathway, and up to assembling an entire bacterial genome. In this context, computational algorithms can help eliminate human error as well as minimise the time and cost of experiments with the ultimate aim of high-throughput fully automated assembly by liquid-handling robots.

## 6.8.1 Computational tools for the automatic implementation of designs based on existing biological parts

The laboratory implementation of a synthetic biology system becomes more complex if one does not really know which parts are needed to build the desired system. In such a situation, tools that (based on a specified model/behaviour) enable either automatic selection of parts or de novo synthesis of DNA sequences are necessary.

Some currently developed tools such as the GEC programming language (Phillips and Cardelli, 2009) can take a high-level description of the desired specifications/behaviour together with a database of standard biological parts with associated properties, and output a set of candidate designs (based on the appropriate choice of parts from the part database) that satisfy the requirements defined in the GEC program. The resulting set of candidate part-based designs can then be numerically simulated for further analysis and selection before the actual experimental implementation.

Another example is ClothoCAD (http://www.clothocad.org/). ClothoCAD is an ambitious large-scale project to develop a modular and integrated software platform for synthetic biology systems providing graphical sequence editing, data management, algorithm management tools and a plug-in system. This software includes the ability to interface with liquid-handling robots for automated production of the designed constructs.

## 6.8.2 Computational tools for the implementation of designs requiring de novo DNA synthesis

Automatic DNA sequence compilers are currently being developed to help synthetic biologists automatically predict the specific DNA sequences that need to be inserted into a chassis cell in order to implement the synthetic biology system that was designed in silico. In particular, current research efforts are focusing on developing calculators or DNA sequence predictors for the most fundamental synthetic biology parts, including promoters, ribosome binding sites, protein coding sequences and terminators. This kind of tool is extremely useful as it provides a link between some high-level property and its low-level implementation within the biomolecular language of the cell. In the future, such tools will provide the currently missing link, allowing the de novo prediction/compilation of DNA sequences required to implement any particular synthetic circuit.

## 6.9 Comparison of Model Predictions/Simulations with In Vivo/In Vitro Data

In order to close the engineering design cycle and to assess the quality of a model and its utility in the design of a synthetic biology system, the predictions of the model need to be compared with experimental data obtained from the in vivo or in vitro implementation of the system (Fig. 6.6).

![](images/page_118_image_2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["biological knowledge"] --> B["construct and revise model"]
  B --> C["model"]
  C --> D["simulate"]
  D --> E["predictions"]
  E --> F["compare"]
  G["data"] --> F
  F --> H["perform and revise experiment"]
  H --> I["biological system"]
  H --> J["biological knowledge"]
```
</details>

Fig. 6.6 Comparing model predictions with experimental data. Models are typically the results of several iterations aimed at refining the model based on these comparisons.

In the design context, in vivo or in vitro testing and characterisation of the synthetic biology construct allows one to feed information back about the behaviour and performance of the implemented systems, allowing for model refinement where necessary. Comparison with the initial design specifications then allows the designer to decide if the implemented systems satisfy the design requirements or if some additional iteration along the design cycle is necessary. Furthermore, predictions of the model may also be informative for the design of new experiments whose goal is to reveal previously unobserved behaviours of the system, thereby deepening its understanding.

## 6.10 Model and/or Experimental Refinements

If the synthetic biology systems implemented in vivo or in vitro do not satisfy the required design specifications or do not behave as predicted by the model, it is necessary to identify the cause of such discrepancy. Several causes of discrepancies must be considered: (i) the model is inappropriate and needs to be revised; (ii) the design specifications are too stringent and need to be relaxed; (iii) the implementation of the synthetic biology construct contains errors that need to be identified and corrected. The first two causes (i) and (ii) launch the synthetic biologist around another full iteration of the engineering design cycle (Fig. 6.1). (iii) requires the use of circuit debugging tools, such as DNA sequencing, and methods for biochemical network reconstruction from data to test if the structure of the implemented synthetic biology circuit corresponds to the one originally intended by its designer.

The approach and concepts that we have briefly introduced in this chapter constitute the main toolbox that engineers typically use to successfully build complex systems by relying on a rational approach based on mathematical modelling, model analysis and in silico simulations prior to actual system implementation. Taking a similar approach in synthetic biology will provide the community with foundational mathematical and computational tools required for the efficient forward-engineering of robust synthetic biology systems of increasing complexity.

## Reading

## Forward engineering:

- Anderson, J, Strelkowa, N, Stan, G-B, et al. (2012). Engineering and ethical perspectives in synthetic biology. EMBO Reports 13(7): 584–590.
- Endy, D. (2005). Foundations for engineering biology. Nature 438: 449–453.
- Galdzicki, M, Clancy, KP, Oberortner, E, et al. (2014). The Synthetic Biology Open Language (SBOL) provides a community standard for communicating designs in synthetic biology. Nat Biotechnol, 32(6): 545—550. doi:10.1038/nbt.2891.
- Kelwick, R, Kopniczky, M, Bower, I, et al. (2015). A forward-design approach to increase the production of poly-3-hydroxybutyrate in genetically engineered Escherichia coli, PLoS ONE 10(2): e0117202. doi: 10.1371/journal.pone.0117202.
- Peccoud, J, Anderson, JC, Chandran, D, et al. (2011). Essential information for synthetic DNA sequences. Nat Biotechnol, 29(1): 22; discussion 22–23. doi:10.1038/nbt.1753.

## Systems and control theory:

- Alon, U. (2007). An Introduction to Systems Biology: Design Principles of Biological Circuits. Chapman & Hall/CRC Mathematical and Computational Biology Series, Boca Raton, FL.
- Iglesias, PA and Ingalls, BP. (2010). Control Theory and Systems Biology. MIT Press, Cambridge, MA.
- Kitano, H. (2001). Foundations of Systems Biology. MIT Press, Cambridge, MA.
- Kulkarni, V, Stan, G-B and Raman, K (Eds) (2014). A Systems Theoretic Approach to Systems and Synthetic Biology I: Models and System Characterizations. Springer, Berlin.
- Kulkarni, V, Stan, G-B and Raman, K (Eds) (2014). A Systems Theoretic Approach to Systems and Synthetic Biology II: Analysis and Design of Cellular Systems. Springer, Berlin.
- Oyarzún, DA and Stan, G-BV (2013). Synthetic gene circuits for metabolic control: design trade-offs and constraints. J R Soc Interface 10(78): 20120671. doi:10.1098/rsif.2012.0671.
- Oyarzún, DA, Lugagne, J-B, and Stan, G-BV (2015). Noise propagation in synthetic gene circuits for metabolic control. ACS Synthetic Biology, 4(2): 116—125. doi:10.1021/sb400126a.
- Wellstead, P, Bullinger, E, Kalamatianos, D, et al. (2008). The rôle of control and system theory in systems biology. Annu Rev Control 32(1): 33–47.

## Engineering design cycle:

- Anderson, J, Strelkowa, N, Stan, G-BV, et al. (2012). Engineering and ethical perspectives in synthetic biology. Rigorous, robust and predictable designs, public engagement and a modern ethical framework are vital to the continued success of synthetic biology. EMBO Reports, 13(7): 584–590. doi:10.1038/embor.2012.81.
- Arpino, JAJ, Hancock, EJ, Anderson, J, et al. (2013). Tuning the dials of Synthetic Biology. Microbiology-SGM, 159: 1236–1253. doi:10.1099/mic.0.067975-0.
- Chandran, D, Copeland, WB, Sleight, SC, et al. (2008). Mathematical modeling and synthetic biology. Drug Discov Today: Disease Models 5(4): 299–309.

## Use of ODEs and SDEs in synthetic biology modelling:

- Algar, R, Ellis, T and Stan, G-BV (2014). Modelling essential interactions between synthetic genes and their chassis cell, Proceedings of the 53rd IEEE Conference on Decision and Control (IEEE CDC 2014), J.W. Marriott Hotel, Los Angeles, CA, USA, 15—17 December, 2014.
- Danino, T, Mondragón-Palomino, O, Tsimring, L, et al. (2010). A synchronized quorum of genetic clocks. Nature 463: 326–330.
- Elowitz, MB and Leibler, S. (2000). A synthetic oscillatory network of transcriptional regulators. Nature 403: 335–338.
- Gardner, TS, Cantor, CR and Collins, JJ. (2000). Construction of a genetic toggle switch in Escherichia coli. Nature 403: 339–342.
- Kaznessis, YN. (2009). Multiscale models for synthetic biology. Conf Proc IEEE Eng Med Biol Soc 6408–6411.
- Purcell, O, Savery, NJ, Grierson, CS, et al. (2010). A comparative analysis of synthetic genetic oscillators. J R Soc Interface 7(52):1503–1024.
- Van Kampen, NG. (2007). Stochastic Processes in Physics and Chemistry. Elsevier, Amsterdam.
- Wilkinson, DJ. (2009). Stochastic modelling for quantitative description of heterogeneous biological systems. Nat Rev Genet 10(2): 122–133.

## Model resolution and parameter identification:

- Gonçalves, J and Warnick, S. (2008). Necessary and sufficient conditions for dynamical structure reconstruction of LTI networks. IEEE Trans Automat Control 53(7): 1670–1674.
- Ljung, L. (1999). System Identification: Theory for the User, 2nd Ed. Prentice Hall, Upper Saddle River, NJ.
- Sontag, ED. (2008). Network reconstruction based on steady-state data. Essays Biochem: Systems Biology 45: 161–176.
- Sontag, ED, Kiyatkin, A and Kholodenko, BN. (2004). Inferring dynamic architecture of cellular networks using time series of gene expression, protein and metabolite data. Bioinformatics 20(12): 1877–1886.
- Yuan, Y, Stan, G-B, Warnick, S, et al. (2010). Network structure reconstruction from noisy data. 49th IEEE CDC, Atlanta, Georgia.

## Bionumbers:

Milo, R, Jorgensen, P, Moran, U, et al. (2010). BioNumbers — the database of key numbers in molecular and cell biology. Nucleic Acids Res 38(Database issue): D750–753.

## Datasheets for biological parts:

Canton, B, Labno, A and Endy, D. (2008). Refinement and standardization of synthetic biological parts and devices. Nat Biotechnol 26(7): 787–793.

## Model selection:

Burnham, KP and Anderson, DR. (2008). Model selection and multimodel inference. Technometrics 45: 18.

## Parameter sensitivity analysis:

- Kiparissides, A, Kucherenko, SS, Mantalaris, A, et al. (2009). Global sensitivity analysis challenges in biological systems modeling. Ind Eng Chem Res 48(15): 7168–7180.
- Kitano, H. (2004). Biological robustness. Nat Rev Gen 5(11): 826–837.
- Lestas, I, Vinnicombe, G and Paulsson, J. (2010). Fundamental limits on the suppression of molecular fluctuations. Nature 467: 174–178.
- Saltelli, A. (2008). Global Sensitivity Analysis: The Primer. John Wiley, Chichester.
- Saltelli, A, Ratto, M, Tarantola, S, et al. (2005). Sensitivity analysis for chemical models. Chem Rev 105(7): 2811–2827.
- Zhou, K, Doyle, JC and Glover, K. (1995). Robust and Optimal Control. Prentice Hall, Upper Saddle River, NJ.
- Ceroni, F, Algar, R, Stan, G-BV, et al. (2015). Quantifying cellular capacity identifies gene expression designs with reduced burden, Nat Methods, 12: 415–418.
- Del Vecchio, D and Murray, R. (2010). Biomolecular Feedback Systems. Available at: http://www.cds.caltech.edu/∼murray/BFSwiki/index.php/Main\_Page [Accessed 24 February 2015].
- Dhooge, A, Govaerts, W, Yu, A, et al. (2003). MATCONT: a MATLAB package for numerical bifurcation analysis of ODEs. ACM Trans Math Software 29(2): 141–164.
- Ermentrout, B. (2003). Simulating, analyzing, and animating dynamical systems: a guide to XPPAUT for researchers and students. Appl Mech Rev 56(4): B53–B53.
- Geva-Zatorsky, N, Rosenfeld, N, Itzkovitz, S, et al. (2006). Oscillations and variability in the p53 system. Mol Syst Biol 2: 2006 0033. Available at: http://msb.embopress.org/content/2/1/2006.0033[Accessed 24 February 2015].
- Heinemann, M and Panke, S. (2006). Synthetic biology — putting engineering into biology. Bioinformatics 22(22): 2790–2799.
- Lestas, I, Vinnicombe, G and Paulsson, J. (2010). Fundamental limits on the suppression of molecular fluctuations. Nature 467: 174–178.
- Macdonald, JT, Barnes, C, Kitney, RI, et al. (2011). Computational design approaches and tools for synthetic biology. Integr Biol, 3(2): 97–108. doi:10.1039/c0ib00077a.
- Meinhardt, H and de Boer, PA. (2001). Pattern formation in Escherichia coli: a model for the poleto-pole oscillations of Min proteins and the localization of the division site. Proc Natl Acad Sci U S A 98(25): 14202–14207.
- Phillips, A and Cardelli, L. (2009). A programming language for composable DNA circuits. J R Soc Interface 6 Suppl 4: S419–436.
- Prindle, A, Samayoa, P, Razinkov, I, et al. (2012). A sensing array of radically coupled genetic ‘biopixels’. Nature, 481(7379): 39–44. doi:10.1038/nature10722.
- Purnick, PEM and Weiss, R. (2009). The second wave of synthetic biology: from modules to systems. Nat Rev Mol Cell Bio 10(6): 410–422.
- Rizk, A, Batt, G, Fages, F, et al. (2009). A general computational method for robustness analysis with applications to synthetic gene networks. Bioinformatics 25(12): 169–178.
- Rodriguez-Fernandez, M and Banga, JR. (2010). SensSB: a software toolbox for the development and sensitivity analysis of systems biology models. Bioinformatics 26(13): 1675–1676.
- Salis, HM, Mirsky, EA and Voigt, CA. (2009). Automated design of synthetic ribosome binding sites to control protein expression. Nat Biotechnol 27(10): 946–950.
- Stricker, J, Cookson, S, Bennett, MR, et al. (2008). A fast, robust and tunable synthetic gene oscillator. Nature 456: 516–519.
- Strogatz, S. (1994). Nonlinear Dynamics and Chaos: with applications to physics, biology, chemistry, and engineering. Perseus Books, New York.
- Thattai, M and van Oudenaarden, A. (2001). Intrinsic noise in gene regulatory networks. Proc Natl Acad Sci U S A 98(15): 8614–8619.
- Turk, G. (1991). Generating textures on arbitrary surfaces using reaction-diffusion. Siggraph 91 Conf Proc 25: 289–298.

## General References:

- Wright, O, Stan, G-BV and Ellis, T. (2013). Building-in biosafety for synthetic biology. Microbiology-SGM, 159: 1221–1235. doi:10.1099/mic.0.066308-0.
- Wright, O, Delmans, M, Stan, G-B, et al. (2014). GeneGuard: A Modular Plasmid System Designed for Biosafety. ACS Synth Biol, 140522150840004. doi:10.1021/sb500234s.
- Zheng, Y and Sriram, G. (2010). Mathematical modeling: bridging the gap between concept and realization in synthetic biology. J Biomed Biotechnol. Available at: http://www.hindawi.com/journals/bmri/2010/541609/ [Accessed 24 February 2015].
- Zi, Z, Zheng, Y, Rundell, AE, et al. (2008). SBML-SAT: a systems biology markup language (SBML) based sensitivity analysis tool. Bioinformatics 9: 342. Available at: http://www.biomedcentral.com/1471-2105/9/342 [Accessed 24 February 2015].

# CHAPTER 7

# Applications of Designed Biological Systems

## 7.1 Introduction

Biological systems surround and pervade every aspect of human existence. It is no surprise that the use of synthetic biology to design living systems will find numerous application areas with significant impact on society. In this chapter we highlight current areas of research on real-world applications, and suggest future areas of investigation.

The use of biological technologies for useful purposes dates back to the emergence of human civilisation itself. For example, humans have used yeast to ferment beer and wine for thousands of years. Today biological technologies are found throughout diverse areas of industry. Synthetic biology promises to accelerate the development of optimised and novel biotechnologies that will be integrated in many aspects of industry and life.

## 7.2 The Potential for Developing Applications of Synthetic Biology

It is often stated that the whole purpose of synthetic biology is to produce applications or products. A recent report (BCCC research BIO066A, published in June 2009) on the commercial potential of synthetic biology forecasts that the expected market for synthetic biology in 2013 would exceed \$2.4 billion. Of this, the chemicals and energy sector is the largest share with a predicted market value of \$1.6 billion, followed by the biotechnology and pharmaceuticals sector with a market share of \$0.6 billion. Growth rates are predicted to be 81% and 49% in these areas, respectively. For this reason a number of major industrial corporations are keenly interested in synthetic biology and what it has to offer.

There are also a host of other reasons for the growing interest in synthetic biology. Because devices can be designed for a specific task or application, unlike naturally occurring organisms that may have many functions, they should, as a technology, function more reliably than non-designed systems and can be optimised for the desired application. In addition, the use and reuse of a set of parts means the cost of characterising sub-assemblies can be shared over a number of products, and will thus be lower than dedicated organisms. Finally, interfaces on both the output and input side can be designed to integrate with existing systems, such as optical sensors and CCD cameras, thus permitting conventional instrumentation to be used rather than biological assays.

## 7.3 Criteria for Developing Applications in Synthetic Biology

Synthetic biology devices are not suitable for all applications, and it is possible to define some criteria for areas where they will be most suitable for commercial development. First, the application area must be sufficiently homogenous to permit one design to work in a wide range of situations. Thus, for example, chemical synthesis is a suitable area, whilst personalised medicine is less suitable because the latter would require a bespoke device for each person. Second, the application area must have a sufficiently large volume to justify the cost of development. Third, the environment that the synthetic system is used in must be compatible with the chassis in which it has been implemented. This is true of most biologically-based processes and should be considered as one of the initial specifications in the design. For example, since many reactions are exothermic, this has led to interest in thermophilic organisms that can withstand the higher temperatures found in fermentation and other process chambers, which is considered preferable to the other option of actively cooling the chamber, since cooling is costly, inefficient and slows down reaction rates. Fourth, the intended application should ideally be constrained to avoid contamination of the synthetic system by external agents, or migration of the system outside the planned sphere of influence. For this reason, industrial biotechnology applications, which constrain the use of the synthetic biological system to inside a reaction vessel, are ideal. Other methods of constraint include adhesion to a surface, particularly suitable for sensor systems. The danger of accidental release of the synthetic system into unintended areas can be minimised through the use of ‘kill’ or fail-safe switches and/or the use of non-living, abiotic chassis which are unable to grow and replicate.

A final consideration in selecting suitable applications for the commercialisation of synthetic biology is public acceptance or at least the absence of public opposition. Some of the factors surrounding this are covered in Chapter 9 and include considerations of public benefit, potential risk and likelihood of direct exposure to the synthetic biological system.

## 7.4 Commercial and Practical Challengest in Application Development

Even if an application is suitable for the use of synthetic biology devices, there are a number of challenges to overcome before it can be implemented. These challenges include competition from existing processes which will be associated with significant pressures to remain in place in the form of previous investment in development and infrastructure. For this reason, synthetic biology approaches to pharmaceutical synthesis will have a harder time replacing existing synthesis routes, however inefficient these may be, as there is not the cost pressure to change. On the other hand, applications in the synthesis of new chemical entities, areas such as biosensors, where there are not chemical or electronic sensors readily available, or in biofuels, where the volumes are such that small improvements in efficiency can have significant cost advantages, will provide a ready area for synthetic biology applications.

Another challenge to be met is the need for robust and efficient scale-up. Most synthetic biology systems are initially developed in a laboratory environment using basic equipment such as shake flasks or 96 well plates at volumes of the order of a few litres or less. These processes must then be transferred first to bench scale reactors and then to pilot plants and industrial scale production, possibly up to tens of thousands of litres per day. Whilst this process occurs regularly in chemical engineering, it is by no means an easy one, often requiring the re-optimisation of experimental conditions at different scales. The cost of this scale-up is part of the investment required to commercialise synthetic biology applications. Fortunately, there are successful examples of how this can be achieved. For example, the biotechnology company Amyris has successfully brought processes for the production of artemisinin and biofuels to an industrial scale. It is important to note that the synthetic biology product must be made in sufficient quantity to meet the whole market, otherwise the market will not be able to rely on the product and will use non-synthetic biology alternatives, eventually eroding the market for the synthetic biology product.

One very pertinent current challenge is the need for validation. In the early years, while synthetic biology is being developed, there is an absence of reliable characterisation data for parts and sub-assemblies, meaning that in early applications, developers will need to perform their own characterisation and absorb the cost that entails. As the field progresses, however, the development of an infrastructure of datasheets for biological parts and chassis will accelerate the commercial development of synthetic systems as lower cost re-use of parts and their associated validation data will be possible.

The presence of a distribution network to transport the product from the factory to the user can also be considered as a potential hurdle. If the synthetic biology product is a living organism, then the environmental constraints for transport and storage will be more demanding than for electronic or chemical products, although not dissimilar to those of packaged sterile medical devices. If the product is a chemical produced by synthetic organisms in the factory, then the compatibility of the synthetic biology-produced chemical with existing distribution networks will aid its substitution. This is a big consideration for potential products such as biofuels, where there is a significant premium for the synthetic biology product to be compatible with existing hydrocarbon fuel stocks. In addition, if the product for distribution is a living synthetic organism, then it must be recognised that public attitudes to risk may demand a greater degree of control over the organism. To this end, a number of groups have introduced parts that stop cell reproduction or can be triggered to cause cell destruction. In summary, activities to overcome these challenges are expected to be a significant element of the continuing development of synthetic biology products and applications in future years. The remainder of this chapter gives details of a number of potential future applications of synthetic biology.

## 7.5 Constructing Microbial Cell Factories

Living systems, from single-celled microbes to complex multicellular organisms, are able to transform simple compounds and nutrients into complex chemicals, materials and structures from the nanoscale to the macroscale. Biological engineers have only just begun to harness natural diversity to produce valuable compounds. The concept of a microbial cell as a ‘factory’ is a useful concept to encapsulate ideas around engineering life as a production platform. For example, much like a factory, cells are able to take material and energy inputs (for example, glucose) and transform them in a step-wise manner to higher value materials. In this analogy enzymes represent the machines in the factory that process and assemble raw materials into finished goods. Microbial cells have been used as factories to produce a wide spectrum of value-added products.

A number of valuable compounds, from small molecules to proteins, are produced by organisms found in nature. However, these are often made by organisms that are not amenable to large-scale industrial growth and production, and are often produced at low yields. To circumvent these issues, bioengineers will express metabolic pathways or proteins in a heterologous host. These hosts include the baker’s yeast Saccharomyces cerevisiae, the model gram negative bacterium Escherichia coli and model mammalian cell lines such as Chinese hamster ovary cells. These production hosts are able to grow rapidly and to high density in fermenters and are genetically tractable. In addition to producing naturally occurring products in heterologous organisms, synthetic biologists are designing cells to produce chemicals, materials and proteins with no natural analogues. This is an example of using biological systems to produce completely synthetic compounds.

## 7.5.1 Protein products

One of the first uses of microbial cells as production platforms was the heterologous production of insulin in E. coli in 1977. The vast majority of human insulin on the market is now produced by bacteria. Protein-based therapeutics (known as biologics in the pharmaceutical industry) is a rapidly growing area of the industry’s portfolio of products that have been approved for the treatment of cancers, inflammatory diseases and cardiovascular disease. In addition to therapeutic proteins, the production of enzymes is an important focus of several industries. These industrial enzymes include proteases, amylases and lipases for food and animal feed processing.

A key step in biologics and protein manufacturing is the production of full-length, functional proteins with high yields in a controlled fermentation process. Proteins are post-translationally modified in many organisms, but the nature and abundance of these modifications differs greatly between organisms. These modifications are important for protein function, and can be complex to implement, so developing production microbes that are able to make the modifications correctly for a given application is a key challenge. The incorporation of synthetic genetic circuits to sense fermenter conditions and control cell growth and metabolism may have significant impact on biologics and enzyme manufacturing. For example, genetically encoded sensors of dissolved oxygen or pH could control the expression of genes involved in central metabolism, rerouting carbon flow to avoid excessive acidification of the process.

## 7.5.2 Fuels

The derivation of liquid transportation fuels from petroleum is one of the most pressing challenges society faces today. Concerns over climate change, limited supplies and the geopolitical costs of oil extraction have driven the search for technologies to transform renewable biomass into fuels. Many organisms, notably baker’s yeast, are able to ferment sugars into ethanol and do so with high productivities. The fermentation of corn sugars to ethanol is currently used to supplement gasoline. However, ethanol has a relatively low energy density and is hygroscopic (takes up water), which presents problems in its distribution and use.

Synthetic biology offers the chance to reprogram organisms to make natural or non-natural compounds which have more favourable fuel characteristics. Recent work has increased the yields of naturally produced compounds such as butanol, but also shown that non-natural fuel compounds can be produced biologically using non-natural combinations of enzymes. These include long-chain diesel-like compounds, short-chain petroleum-like compounds, and gaseous propane.

## 7.5.3 Commodity chemicals

In addition to liquid transportation fuels, there is a demand for renewable sources of commodity chemicals. Commodity chemicals are broadly defined as low molecular weight precursors of high value industrial chemicals. These are also known as ‘platform chemicals’, because they provide a common set of building blocks that the chemical industry can use to produce a diverse range of valuable products. Examples include ethylene, propylene and butadiene, which are produced in millions of tons per year to synthesise plastics, resins and other materials.

There have been several synthetic approaches to producing commodity chemicals from renewable biomass. DuPont has commercialised a genetically modified E. coli that produces 1,3-propanediol (1,3-PDO) from corn syrup. 1,3-PDO is used to make polyesters, composites, laminates and coatings. The biological process uses a renewable carbon source and uses 40% less energy than the conventional process. Synthetic biological routes to valuable compounds often have advantages in process energy costs, due to the fact that biological systems (enzymes and metabolic processes) operate close to room temperature and at standard pressure.

## 7.5.4 Materials

Many protein-based biological materials have physical properties that exceed even the most high performance man-made polymers. Some of the most well-known examples are spider silks. Spider silks are made from proteins containing highly repetitive proline-rich helical domains. Silks are able to stretch to many times their length without failure and have tensile strengths exceeding that of Kevlar®. Due to the difficulties in farming and harvesting silk protein from spiders, there is significant interest in producing silks in microbial cells. This presents particular challenges: highly repetitive proteins often express poorly in recombinant hosts due to inefficient codon usage. To solve this, several researchers have used chemical gene synthesis to construct synthetic spider silk genes for expression in bacteria. These genes have identical amino acid sequences to native spider silks, but are computationally codon-optimised for production in fast-growing microbes such as E. coli. The ‘recoding