# AI Output Evaluation and Content Accuracy Review

**I spent 13 years checking whether documents said what they were supposed to say before money moved. I now apply the same habit to evaluating AI-assisted content and output.**

Bilingual English and Spanish. Based near Toronto, available for remote contract work.

---

## Relevant skills

- AI output evaluation and factual verification
- Document accuracy and consistency review
- Guideline and rubric-based quality control
- Evidence and source verification
- Contract and transaction document review
- English and Spanish content review
- SQL data validation

---

## Why I am a fit for this work

Annotation and output review requires three things: following guidelines precisely, distinguishing correct information from plausible-sounding errors, 
and maintaining accuracy across repetitive work.

Those are the habits I built over 13 years reviewing regulated real estate transaction files. Every file had to be verified against contracts, 
disclosures, and supporting documents before it could close. Missing an inconsistency was not a small mistake. A missing amendment or a mislabeled 
condition does not announce itself. It surfaces after closing, when correcting it is far more costly than catching it would have been, and it is the 
kind of error a licensed agent can be held liable for. Across more than 100 transactions, I had no material audit findings. In plain terms, no file I 
handled was later found to contain an error.

The work required careful reading, comparing one document against another, and flagging anything that did not line up. I was good at it because I 
found it satisfying rather than tedious.

What that gives me for this work:

- Consistency across volume. Multiple files open at once, each with its own conditions and deadlines, accuracy on the last one the same as the first.
- A habit of checking rather than assuming. If a figure appears twice and the two do not match, I go find out which one is wrong.
- Comfort saying something is wrong. Flagging problems was my job for over a decade.
- English and Spanish.

---

## A real example, including the parts that did not go well

Over several months I built a technical portfolio documenting a cloud cost investigation. I performed the analysis, created the evidence artifacts, 
and used AI tools as a drafting and review assistant throughout the process while independently validating the final content. The executive summary 
and full technical investigation are available in my GitHub portfolio: [FinOps Cost Allocation Gap Summary](https://github.com/AthertHa-FinOps/finops-cost-allocation-gap-summary) and [AWS FinOps Cost Allocation Investigation](https://github.com/AthertHa-FinOps/aws-finops-cost-allocation-investigation).

I ran repeated accuracy reviews on my own documents during that process. They found real problems.

**Claims that outran the evidence.** An early version said alerts were being delivered to a chat channel. They were not. The code built the alert, 
wrote it to a log, and nothing sent it anywhere. The document said one thing and the artifact said another. I rewrote every affected section to 
separate what was built from what was only designed.

**Figures that did not reconcile.** The document reported one total in one place, and a different total when you added up the component parts. Neither 
was flagged as uncertain. Both were presented as fact. I rebuilt the arithmetic from the underlying evidence and propagated the corrected figure 
through every table and both documents.

**A screenshot that contradicted its own caption.** A caption described two bug fixes in a piece of code. The code in the image contained neither fix. 
Anyone reading the code before the prose would have caught it in seconds. I rewrote the caption to describe what the image actually showed.

**Two documents drifting apart.** A summary and a full report were maintained separately. Over time the summary began claiming things the full report 
explicitly disclaimed. Each was internally consistent. Together they contradicted each other.

I describe these openly because finding this class of error is the skill, not something to hide. Content that is fluent, well-structured, and 
confidently written is exactly where inaccuracies survive longest. Nobody double-checks a sentence that reads well.

---

## The framework I built to stop it recurring

I built an evidence labelling system and applied it to every claim and image in the portfolio:

| Label | Meaning |
|---|---|
| **Captured** | Real output from the source system, real data |
| **Executed** | Real query run against a constructed dataset |
| **Illustrative** | Constructed output demonstrating logic and result shape |
| **Modelled** | Scenario reasoning, no underlying data |
| **Methodology** | Design and provenance artifacts |

Every screenshot carries its label, and the tense of the surrounding prose follows it. Past tense for captured evidence only, present tense for 
demonstrations, conditional for modelled scenarios. Anything that could not be verified is listed in a limitations section at the end.

AI-generated content does not reliably distinguish between verified information, generated assumptions, and unsupported claims. Someone has to 
evaluate the evidence, classify the claim, and label it honestly.

---

## Sample evaluation

Three AI-generated statements about a topic I know well, evaluated the way I would evaluate them in a review queue.

### Statement 1

> "AWS Cost and Usage Reports include all resource tags by default, so you can immediately break down spend by team."

**Incorrect.**

Tags do not appear in the Cost and Usage Report until they are activated as cost allocation tags in the Billing console. That is a separate, 
deliberate step. Until it happens, the tag columns do not exist in the report schema at all.

**Why it matters:** The statement is wrong in a way that produces a confident and incorrect analysis. Someone acting on it would query for tag data, 
get empty columns, and conclude the resources are untagged when they may be tagged correctly. The error is downstream and invisible.

**Correction:** Tags must first be activated as cost allocation tags in the Billing console before they appear in the Cost and Usage Report.

### Statement 2

> "A resource missing one of three required tags is partially compliant, which is better than a resource missing all three."

**Misleading. Correct in one sense, wrong in the sense that matters.**

For remediation it is true. A resource with two of three tags still tells you who owns it, so you know who to ask. For reporting it is false. A report 
grouping by the missing field drops those records entirely, or files them under unknown. The cost does not reach the responsible team either way.

**Why it matters:** This is the harder category. The statement is not factually false, so a reviewer skimming for errors lets it through. It is 
misleading because it implies a difference in outcome that does not exist where it counts.

**Correction:** Distinguish the two cases. Partial tagging is easier to remediate and produces the same reporting gap as no tagging.

### Statement 3

> "AWS Config can tell you whether a resource was created without required tags or had its tags removed later."

**Incorrect.**

Config evaluates resource state. It records what a resource looks like and compares it against a rule. It cannot reconstruct the original API request, 
so it cannot distinguish tags that were never submitted from tags applied and later removed. CloudTrail records the request itself, including tags 
submitted at creation, so it can answer that.

**Why it matters:** The distinction changes what you do. Never applied means the fix belongs at provisioning. Removed later means the fix is 
monitoring and cleanup. An answer that conflates them sends someone toward the wrong remediation.

**Correction:** Config evaluates current state. CloudTrail records the original request, which is what distinguishes tags absent at creation from tags 
removed afterward.

---

**What these three are meant to show.** The first is a straightforward factual error. The second is technically accurate and still misleading, which 
is the harder and more common case. The third is wrong in a way that leads to a wrong decision rather than just a wrong fact. Those need different 
flags and different explanations, and telling them apart is most of the job.

---

## Español

Durante trece años trabajé revisando documentos y contratos en transacciones inmobiliarias reguladas. Cada expediente tenía que cuadrar con los 
contratos y la documentación de respaldo antes de poder cerrarse. Mi trabajo era encontrar lo que no cuadraba y corregirlo antes de que se convirtiera 
en un problema.

Puedo trabajar en inglés y español en revisión de contenido, anotación y evaluación de calidad.

### Ejemplo de evaluación

> "Una propiedad puede cerrarse aunque una condición del contrato siga pendiente, mientras las partes estén de acuerdo."

**Incorrecto.**

Una condición pendiente tiene que cumplirse o eliminarse formalmente por escrito antes del cierre. Un acuerdo verbal entre las partes no reemplaza una 
enmienda firmada. Si el expediente se cierra con la condición todavía abierta, el problema no aparece de inmediato. Aparece después, cuando resolverlo 
ya sale mucho más caro.

**Por qué importa:** La afirmación suena razonable, y por eso es fácil dejarla pasar. El error no está en cómo está dicho, sino en el orden en que 
deberían hacerse las cosas. Alguien que actúe sobre esta información va a llegar a la conclusión equivocada.

**Corrección:** Toda condición tiene que cumplirse o eliminarse mediante una enmienda escrita y firmada antes del cierre, no después.

---

## How I use AI tools

- **AI Fluency: Framework and Foundations**, Anthropic, March 2026
- Several months of daily practical use of AI tools for research, drafting, document review, and iterative editing on a substantial technical
portfolio project
- Salesforce Trailhead: Agentforce 360 Platform Basics, AgentExchange Basics
- Documented experience identifying and correcting inaccuracies in AI-assisted output, described above

I am comfortable working alongside these tools and comfortable disagreeing with them. Both matter here.

---

## What I have not done

Accuracy requires being clear about both experience and limitations.

- I have not worked professionally as an annotator or content reviewer.
- I have not worked under a formal commercial annotation guideline or rubric.
- My AI experience is as a working user, not a machine learning practitioner. I do not have a technical background in model training or development.
- The evaluation examples above are my own portfolio work, written to demonstrate my approach. They are not samples from a professional annotation
project.

What I do have is 13 years of reviewing regulated transaction documents where accuracy and completeness were required before a transaction could 
proceed, including peer review of files prepared by other professionals. Identifying inconsistencies before they affected the transaction was a core 
responsibility.

---

## Background

- 13 years reviewing regulated real estate transaction files, 100+ transactions, zero material audit findings
- AWS Certified Cloud Practitioner
- AI Fluency: Framework and Foundations, Anthropic
- Introduction to FinOps, FinOps Foundation
- SQL for Data Science, UC Davis via Coursera
- Technical Support Fundamentals, Google

---

## What I am looking for

Remote contract or full-time opportunities in cloud cost analysis, IT financial analysis, or IT asset management, as well as AI output evaluation, 
data annotation, quality review, or bilingual content review. Available immediately for remote contract assignments, including project-based and high-
volume review work. Comfortable with rubric-based and guideline-driven evaluation.

---

## Portfolio Links

- [AI Output Evaluation & Content Accuracy Review](https://github.com/AthertHa-FinOps/AI-Output-Evaluation-Content-Accuracy-Review)
- [FinOps Cost Allocation Gap Summary](https://github.com/AthertHa-FinOps/finops-cost-allocation-gap-summary)
- [AWS FinOps Cost Allocation Investigation](https://github.com/AthertHa-FinOps/aws-finops-cost-allocation-investigation)

**Contact:** hans.atherton@gmail.com
**LinkedIn:** [Hans Atherton](https://www.linkedin.com/in/hans-atherton-82638234/)
