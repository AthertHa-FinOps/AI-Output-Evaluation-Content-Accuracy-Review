# AI Output Evaluation & Content Accuracy Review

**Hans Atherton · Self-directed AI evaluation and document-quality portfolio**

**I spent 13+ years checking whether documents said what they were supposed to say before money moved. I now apply the same habit to 
evaluating AI-assisted content and output.**

Bilingual English and Spanish. Based near Toronto and available for remote contract work.

> **Privacy note:** Every personal record, name, number, and transformed-data example created specifically for this portfolio is synthetic or
fully redacted. No real client or personal information appears in this repository.

---

## Related portfolio work

- [FinOps Cost Allocation Gap Summary](https://github.com/AthertHa-FinOps/finops-cost-allocation-gap-summary)
- [AWS FinOps Cost Allocation Investigation](https://github.com/AthertHa-FinOps/aws-finops-cost-allocation-investigation)

---

## Relevant skills

- AI output evaluation and factual verification
- Document accuracy and consistency review
- Guideline and rubric-based quality control
- Evidence and source verification
- Personally identifiable information (PII) awareness
- Data-integrity and discrepancy review
- Contract and regulated transaction document review
- Findings documentation and rationale
- English and Spanish content review
- SQL data validation

---

## Why I am a fit for this work

AI output and document review require three things: following requirements precisely, distinguishing correct information from plausible-
sounding errors, and maintaining accuracy across repetitive work.

Those are the habits I built over 13+ years reviewing regulated real estate transaction files. Every file had to be checked against 
contracts, disclosures, identity documentation, financial information, and supporting records before it could move forward. Missing 
information, inconsistent figures, or conflicting documents had to be identified and resolved before contractual and financial deadlines.

Across more than 100 transactions, none of my files resulted in a material audit finding.

The work required careful reading, comparing one document against another, tracing discrepancies back to source records, and flagging 
information that did not line up. I was good at it because I found that kind of review satisfying rather than tedious.

What that gives me for AI and document-quality work:

- **Consistency across concurrent files.** Multiple files can be open at once, each with different documents, conditions, and deadlines. The
last review still needs the same care as the first.
- **A habit of checking rather than assuming.** If a figure appears twice and the two values do not match, I want to know which source
supports the correct one.
- **Comfort flagging problems.** Identifying incomplete, inconsistent, or unsupported information was a core part of my professional work.
- **Clear rationale.** A finding is more useful when it explains what is wrong, what evidence supports that conclusion, and what should
happen next.
- **English and Spanish.**

---

## A real example, including the parts that did not go well

Over several months I built a technical portfolio documenting a cloud-cost investigation. I performed the analysis, created the evidence 
artifacts, and used AI tools as a drafting and review assistant throughout the process while independently validating the final content.

The executive summary and full technical investigation are available here:

- [FinOps Cost Allocation Gap Summary](https://github.com/AthertHa-FinOps/finops-cost-allocation-gap-summary)
- [AWS FinOps Cost Allocation Investigation](https://github.com/AthertHa-FinOps/aws-finops-cost-allocation-investigation)

I ran repeated accuracy reviews on my own documents during that process. They found real problems.

### Claims that outran the evidence

An early version said alerts were being delivered to a chat channel. They were not.

The code built the alert and wrote it to a log, but nothing actually sent it anywhere. The document said one thing and the artifact 
demonstrated another.

I rewrote the affected sections to separate what had actually been built from what was only proposed or designed.

### Figures that did not reconcile

One document reported a total that did not match the sum of its component values.

Both numbers were presented confidently, and neither was marked uncertain.

I rebuilt the arithmetic from the underlying evidence and propagated the corrected figure through the affected tables and documents.

### A screenshot that contradicted its own caption

A caption described two fixes that were supposedly visible in a piece of code.

The code shown in the screenshot contained neither fix.

Someone reading the image before the prose could have identified the contradiction immediately.

I rewrote the caption so that it described only what the screenshot actually supported.

### Two documents drifting apart

A summary document and a full technical report were maintained separately.

Over time, the summary began claiming things that the full report explicitly disclaimed.

Each document was internally consistent. Read together, however, they contradicted one another.

I describe these problems openly because finding this class of error is the skill I want the portfolio to demonstrate.

Content that is fluent, organized, and confidently written can still be unsupported by its evidence. Those are often the claims that most 
need deliberate review.

---

## The framework I built to stop it recurring

I built an evidence-labelling system and applied it to claims and images in the technical portfolio:

| Label | Meaning |
| --- | --- |
| **Captured** | Real output captured from the source system or real source data |
| **Executed** | Real query or process executed against a constructed dataset |
| **Illustrative** | Constructed output demonstrating logic, method, or expected result shape |
| **Modelled** | Scenario reasoning without underlying executed data |
| **Methodology** | Design, process, or provenance documentation |

The label controls how strongly I can describe the evidence.

Past tense is reserved for things actually captured or executed. Demonstrations are described as demonstrations. Modelled scenarios remain 
conditional. Claims that cannot be verified are not presented as completed results.

AI-assisted content does not reliably distinguish between verified evidence, assumptions, demonstrations, and unsupported claims.

Someone still has to inspect the source, evaluate the claim, classify the evidence, and describe it accurately.

---

## Review method

This is the review process I use in the exercises in this repository.

### 1. Define the requirement

Before evaluating an output, identify what it is supposed to contain, preserve, remove, or communicate.

If the requirement is ambiguous, record the ambiguity rather than silently choosing an interpretation.

### 2. Define the review sample

When reviewing a larger set, establish the sample before reviewing rather than selecting only records that already look suspicious.

A repeatable sample can then be supplemented with targeted checks of unusual or higher-risk records.

### 3. Verify against source evidence

Trace claims, values, dates, labels, and other important information back to the available source.

A claim without supporting evidence is flagged even when it sounds plausible.

### 4. Classify the issue

Examples used in this portfolio include:

- factual error
- unsupported claim
- internal inconsistency
- missing information
- data-integrity issue
- formatting inconsistency
- privacy / PII exposure
- instruction or requirement mismatch

### 5. Rate severity

| Severity | Meaning |
| --- | --- |
| **High** | Information is exposed or materially wrong in a way that could cause harm, compromise privacy, or lead to a materially incorrect 
decision |
| **Medium** | Information is incorrect, unsupported, missing, or inconsistent but is unlikely to cause serious harm by itself |
| **Low** | Formatting, wording, or presentation issue that does not materially change the underlying meaning |
| **Pass** | Reviewed item meets the stated requirement |

Severity depends on context. The same error can have different consequences in different workflows.

### 6. Document the rationale

A useful finding should answer:

- What did I review?
- What did the output say or contain?
- What does the source or requirement support?
- What is wrong or missing?
- Why does it matter?
- What correction or follow-up is appropriate?

### 7. Follow through

Where a correction is required, the review is not complete merely because the problem was identified.

The issue should either be corrected, escalated, or explicitly accepted.

---

## Transformed-record spot-check

**Label: Illustrative — synthetic exercise**

**All names, identifiers, numbers, and records below are fictional. This is not production work or client data.**

This exercise demonstrates how I would review a record after transformation for missed sensitive information, inconsistent formatting, and 
incomplete masking.

### Transformation requirements

For this exercise, the transformation is supposed to:

1. mask names wherever they appear;
2. fully mask the ID number;
3. expose only the final four digits of the phone number;
4. preserve the date format as `YYYY-MM-DD`; and
5. remove direct identifiers from free-text fields.

### Source record

| Field | Value |
| --- | --- |
| Name | Jane Sample |
| Phone | 416-555-0142 |
| ID number | ID-000000 |
| Date of birth | 1990-05-14 |
| Notes | Jane called on May 3 to confirm her address. |

### Transformed record

| Field | Value |
| --- | --- |
| Name | J*** S***** |
| Phone | ***-***-0142 |
| ID number | ID-000000 |
| Date of birth | 14/05/1990 |
| Notes | Jane called on May 3 to confirm her address. |

### Findings

| ID | Finding | Type | Severity | Rationale |
| --- | --- | --- | --- | --- |
| T-01 | ID number remains unmasked | Privacy / PII | **High** | The transformation required the identifier to be fully masked, but the 
original value remains exposed. |
| T-02 | Name remains visible in the free-text Notes field | Privacy / PII | **High** | Masking the structured Name field did not remove the 
same identifier from another field. |
| T-03 | Date changed from `YYYY-MM-DD` to `DD/MM/YYYY` | Formatting / consistency | **Low** | The output does not preserve the required date 
format. |
| T-04 | Phone exposes only the final four digits | Pass | **Pass** | The result matches the stated phone-masking requirement. |

### Qualitative review

**Question: Was the transformation complete?**

**Answer: No.**

Two privacy exposures remain: the ID number and the name in the free-text Notes field. The date format also fails the stated transformation 
requirement.

I would hold this record for correction.

I would also expand the review to other free-text fields in the batch because the failure to remove the name from Notes suggests that the 
transformation may be masking structured fields without detecting the same information in unstructured text.

### Review decision

**Fail — correction required before acceptance.**

The two high-severity findings prevent the record from passing even though one masking requirement was completed correctly.

This example is illustrative rather than professional production work. Its purpose is to demonstrate the review method I would apply to 
transformed records containing sensitive information.

---

## Sample AI-output evaluation

The following examples show how I distinguish between straightforward factual errors, context-dependent claims, and claims that overstate 
what the available evidence can establish.

---

### Statement 1

> "AWS Cost and Usage Reports include all resource tags by default, so you can immediately break down spend by team."

**Incorrect.**

Applying a tag to a resource does not automatically make that tag available for cost-allocation reporting. Relevant user-defined tag keys 
must be activated as cost allocation tags before they can be used in AWS cost-allocation reporting.

**Why it matters:** Someone who assumes every resource tag automatically appears in billing data could interpret missing cost-allocation data 
as a resource-tagging failure when the reporting configuration itself may be incomplete.

**Correction:** Applying a resource tag and making that tag available for cost allocation are separate steps. Relevant tag keys must be 
activated for cost-allocation reporting before they can be used to categorize those costs.

---

### Statement 2

> "A resource missing one of three required tags is partially compliant, which is better than a resource missing all three."

**Context-dependent and potentially misleading.**

For remediation, the distinction can matter.

A resource that still has an ownership tag may be easier to investigate because there is evidence of who is responsible for it.

For a report grouped by the missing tag, however, both a partially tagged resource and a completely untagged resource can still create an 
allocation gap for that dimension.

**Why it matters:** The statement can be true from one operational perspective while implying a reporting advantage that does not necessarily 
exist.

**Correction:** Partial tagging may make remediation easier, but whether it improves reporting depends on which required tag is missing and 
how the report uses that field.

---

### Statement 3

> "AWS Config can tell you whether a resource was created without required tags or had its tags removed later."

**Incomplete / potentially misleading.**

AWS Config records observed resource configuration state over time and can show configuration changes captured in the resource history.

It does not record the original API request that created or modified the resource.

CloudTrail records API activity and request parameters, making it the stronger evidence source when the question depends on what was actually 
submitted in a creation or modification request.

**Why it matters:** The distinction affects remediation.

If required tags were absent during provisioning, the problem may be in the creation workflow.

If tags existed and were later removed, the problem may instead involve permissions, monitoring, or post-provisioning changes.

The evidence needs to support that distinction before assigning a cause.

**Correction:** Use AWS Config to examine recorded resource-state changes over time and CloudTrail when the analysis depends on API activity 
or request parameters.

---

## What these examples are meant to show

The first is a straightforward factual error.

The second is more difficult because it can be correct from one perspective and misleading from another.

The third shows how an answer can overstate what one evidence source can establish.

Those situations require different flags, different evidence checks, and different explanations.

The goal is not simply to label something "right" or "wrong." The goal is to determine what the evidence actually supports and explain the 
difference clearly.

---

## Español

Durante más de trece años trabajé revisando documentos y expedientes de transacciones inmobiliarias reguladas.

Cada expediente tenía que concordar con los contratos y la documentación de respaldo antes de poder avanzar. Parte de mi trabajo consistía en 
identificar información incompleta o contradictoria y seguir el problema hasta que se corrigiera.

Puedo trabajar en inglés y español en revisión de contenido, evaluación de calidad y verificación de información.

### Ejemplo de evaluación — transacción inmobiliaria en Ontario

> "Una propiedad puede cerrarse aunque una condición del contrato siga pendiente, mientras las partes estén de acuerdo."

**Incorrecto / demasiado amplio.**

Una condición pendiente debe resolverse conforme a los términos del acuerdo. Dependiendo de la condición y del contrato, la documentación 
correspondiente puede incluir, por ejemplo, una renuncia, una notificación de cumplimiento o una enmienda.

Un acuerdo verbal por sí solo no sustituye la documentación contractual que corresponda.

**Por qué importa:** La afirmación parece sencilla, pero convierte un proceso que depende de los términos del contrato en una regla general. 
Una persona que actúe sobre esa simplificación podría proceder sin confirmar que la condición fue resuelta y documentada correctamente.

**Corrección:** Una condición pendiente debe resolverse conforme al acuerdo y documentarse mediante el instrumento que corresponda, por 
ejemplo una renuncia, una notificación de cumplimiento o una enmienda, según corresponda.

---

## How I use AI tools

- **AI Fluency: Framework & Foundations**, Anthropic, 2026
- Several months of practical use of AI tools for research, drafting, document review, comparison, and iterative editing during technical
portfolio work
- Independent verification of AI-assisted content against source evidence
- Documented examples of identifying unsupported claims, inconsistent totals, evidence/caption mismatches, and contradictions between
documents
- Structured use of evidence labels to distinguish captured results, executed demonstrations, illustrative outputs, modelled scenarios, and
methodology

I am comfortable working with AI tools, but I do not treat fluent output as verified output.

The review still has to establish what the available evidence supports.

---

## What I have not done

Accuracy requires being clear about both experience and limitations.

- I have not worked professionally as an AI annotator or AI content reviewer.
- I have not worked under a formal commercial annotation guideline or production evaluation rubric.
- I have not performed production PII-redaction or transformed-record QA for an AI company.
- The transformed-record exercise in this repository is synthetic and illustrative.
- My AI experience is as a working user and self-directed evaluator, not as a machine-learning practitioner.
- I do not have a professional background in model training or model development.
- The AI evaluation examples in this repository are portfolio work unless specifically identified as observations from my own technical
projects.

What I do have is 13+ years of professional experience reviewing regulated transaction documents where accuracy and completeness were 
required before files could proceed, including peer review of files prepared by other professionals and investigation of missing or 
conflicting information.

---

## Background

- 13+ years reviewing regulated real estate transaction documentation
- 100+ regulated property transactions
- Zero material audit findings
- Professional review of identity, financial, contractual, compliance, and supporting documentation
- Peer review of files prepared by other professionals
- Discrepancy investigation and corrective follow-through
- English and Spanish
- AWS Certified Cloud Practitioner
- AI Fluency: Framework & Foundations — Anthropic
- SQL for Data Science — UC Davis / Coursera
- Technical Support Fundamentals — Google

---

## What I am looking for

Remote contract or full-time opportunities in:

- AI output evaluation
- document review
- data quality
- quality assurance
- data annotation
- content-quality review
- bilingual English/Spanish review

I am also open to cloud-cost analysis, IT financial analysis, and related technology-adjacent work where my technical portfolio is relevant.

Available immediately for project-based and high-volume review assignments.

Comfortable working from detailed guidelines, evaluation rubrics, evidence requirements, and structured quality-review procedures.

---

## Project limitations

This is a small, self-directed portfolio project.

It demonstrates how I approach evidence verification, document quality, transformed-record review, discrepancy classification, qualitative 
reasoning, and correction.

It does **not** represent:

- paid AI annotation experience;
- a production model-evaluation environment;
- a measured commercial error rate;
- production PII transformation work;
- inter-rater agreement with other reviewers; or
- throughput results from a commercial review queue.

The transformed-record example is synthetic.

The AWS examples are based on a technical domain I have studied and used in my own portfolio work.

Future expansion could include additional synthetic transformed records, larger review batches, a structured findings log, and repeated test 
runs using the same rubric to measure consistency.

The purpose of this repository is not to imply experience I do not have.

It is to make my review method visible.
