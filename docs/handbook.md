
generate me a mock handbook for me (i am making a rag model)

Created and edited larkspur_employee_handbook.md, ran a command
I’ve written the mock handbook as a Markdown file: larkspur_employee_handbook.md. It’s an employee handbook for a made-up logistics software company, Larkspur Freight Systems, at about 5,300 words. It has 12 numbered sections, 4 appendices and 23 tables, and covers time off, pay, benefits, expenses, security, conduct, performance and leaving. Its section headings should make it easy to split into chunks.

I also included some details that tend to trip up RAG systems:

Challenge	Example question	Where the answer is
Answers that depend on region	“How much PTO do I get in the UK after 4 years?”	Row and column lookup in the §5.1 table
Exceptions to a general rule	“How many office days are required?”	2 days, but 3 for Manchester Customer Support (§4.2)
Information split across sections	“Can a new hire work abroad?”	Rule in §4.4, probation lengths in §3.2
Outdated values	“What’s the US learning budget?”	$1,500 in §7.5; the old $1,000 is in Appendix C
Similar-looking facts	“How long do I have to submit an expense?”	30 days in §8.1, but other 30-day and 14-day limits appear throughout
Made-up terms	“What is Trellis?”	Glossary in Appendix A; useful for testing keyword versus embedding search
Questions it can’t answer	“What’s the pet insurance policy?”	Not in the handbook, so the model should say it doesn’t know
All the names, numbers and policies are invented, and the emails and phone numbers are placeholders (.example domains and 555 numbers). A model that answers from these details is using the document, not its general knowledge.

If you want to keep this work, I can move this session to a folder you choose.

Your mock employee handbook is written as a Markdown file for a fictional company, at about 5,300 words. It hasn't been run through a RAG pipeline yet.

Want a question set with expected answers for testing retrieval?



Larkspur Freight Systems — Employee Handbook
Version: 4.2 Effective date: July 1, 2026 Policy owner: People Operations Next scheduled review: January 2027

Larkspur Freight Systems is a fictional company. This handbook is mock data created for testing. It is not legal, HR, or financial advice.

1. About This Handbook
1.1 Purpose
This handbook describes the policies, benefits, and expectations that apply to employees of Larkspur Freight Systems, Inc. and its subsidiaries ("Larkspur" or "the Company"). It replaces all earlier versions. Changes from earlier versions are listed in Appendix C.

1.2 Who it covers
This handbook applies to all regular full-time and part-time employees in the United States, the United Kingdom, and Canada. Contractors and agency workers are governed by their service agreements, except that Section 9 (Information Security) and Section 10 (Code of Conduct) apply to anyone with access to Larkspur systems or premises.

1.3 Regional differences and precedence
Where a policy differs by country, the regional rule is stated in the relevant section. If this handbook conflicts with an employment contract, the contract takes precedence. If either conflicts with local law, local law takes precedence.

1.4 Not a contract
For US employees, nothing in this handbook creates a contract of employment or changes at-will status. For UK and Canadian employees, this handbook is non-contractual unless a section expressly says otherwise.

2. Our Company
2.1 Overview
Larkspur builds routing, dock scheduling, and carrier billing software for mid-sized freight operators. The Company was founded in Denver, Colorado in 2011 by Maren Okafor and Tomas Lindqvist. Larkspur employs about 640 people and serves more than 1,100 customers. Its flagship product is Larkspur Dispatch, and its newer analytics product is Larkspur Lens, launched in 2023.

2.2 Offices
Office	Region	Role	Opened
Denver, Colorado	US	Global headquarters	2011
Manchester, England	UK	EMEA headquarters, Customer Support	2017
Toronto, Ontario	Canada	Platform Engineering hub	2020
2.3 Values
Larkspur has four values, known internally as the Four Bearings:

Ship the load. Finish what you commit to, and flag early when you can't.
Read the whole manifest. Understand the context before making a decision.
Share the road. Help other teams, and give credit freely.
Leave the dock cleaner. Improve the systems and processes you touch.
2.4 Leadership
Role	Name
Chief Executive Officer	Maren Okafor
Chief Technology Officer	Tomas Lindqvist
Chief People Officer	Dolores Vance
Chief Financial Officer	Rajiv Menon
Chief Information Security Officer	Hana Sorensen
General Counsel	Peter Adeyemi
3. Employment Basics
3.1 Employment classifications
Regular full-time: scheduled for 30 or more hours per week. Eligible for all benefits.
Regular part-time: scheduled for 20 to 29 hours per week. Eligible for prorated PTO and for health coverage, but not for equity grants.
Fixed-term: employed for a defined period of 12 months or less. Eligible for PTO and statutory benefits, but not for the annual bonus or equity grants.
Intern: employed for a program of up to 16 weeks. Not eligible for benefits other than those required by law.
Employees scheduled for fewer than 20 hours per week are eligible only for benefits required by law.

3.2 Probationary period
New employees complete a probationary period, during which either party may end employment on shortened notice (see Section 12.1).

Region	Length
US	90 calendar days
Canada	90 calendar days
UK	6 months
A manager may extend probation once, by up to 30 calendar days, with People Operations approval. Employees on probation cannot use the Work From Abroad policy (Section 4.4) or apply for an internal transfer.

3.3 Background checks
Offers are conditional on a background check completed before the start date. Roles with access to Restricted data (Section 9.2) also require a re-check every 3 years.

3.4 Internal transfers
Employees may apply for internal roles after 12 months in their current role. An employee must tell their current manager before the final interview stage. Employees on a Performance Improvement Plan are not eligible.

3.5 Employee levels
Larkspur uses levels L1 to L7 for individual contributors and managers, followed by Director (D), Vice President (VP), and C-level. Your level appears in your profile in Trellis, the Company's HR system.

4. Working Hours and Location
4.1 Core hours
Full-time employees typically work 40 hours per week in the US and Canada, and 37.5 hours per week in the UK. Core collaboration hours are 10:00 a.m. to 3:00 p.m. local office time, Monday to Friday. Customer Support and on-call staff follow their published rotas instead of core hours.

4.2 Hybrid work
Employees who live within 50 miles (80 km) of an office are hybrid and work from the office at least 2 days per week. The anchor days are Tuesday and Thursday. Employees who live farther away are remote, and are expected to visit their assigned office at least twice a year at Company expense.

Customer Support staff in Manchester are an exception and work from the office 3 days per week, on days set by their team lead.

4.3 Home office support
Benefit	US	UK	Canada
One-time home office stipend	$600	£450	C$800
Monthly internet allowance	$50	£40	C$65
The stipend is available to both hybrid and remote employees and may be claimed once during employment, within the first 6 months. The internet allowance is available to remote employees only and is paid through payroll.

4.4 Work From Abroad
Employees may work from outside their country of employment for up to 20 working days per calendar year. These days do not need to be consecutive, and unused days do not carry over. Requests must be submitted in Trellis at least 15 business days before travel and approved by both the employee's manager and People Operations.

Work From Abroad is not available:

during probation;
in any country on the Restricted Travel List maintained by Legal;
to employees who handle Restricted data, unless the CISO grants a written exception;
to Platform Engineering and Customer Support staff during the Peak Season Freeze (Section 5.5).
4.5 On-call
Engineers on the on-call rota receive a stipend of $400, £320, or C$540 per week on call. An employee who is paged between 10:00 p.m. and 6:00 a.m. local time may start up to 3 hours later the next working day. Time worked responding to a Severity 1 incident on a weekend or public holiday earns one day of time off in lieu, which must be used within 60 days.

5. Time Off
5.1 Paid time off (PTO)
PTO accrues monthly and is based on length of service, measured from the start date. UK figures exclude the 8 public holidays, which are additional.

Length of service	US	Canada	UK
Under 3 years	18 days	20 days	25 days
3 to under 6 years	21 days	22 days	26 days
6 years or more	25 days	25 days	28 days
Part-time employees accrue PTO in proportion to their scheduled hours.

5.2 Carryover
Employees in all regions may carry over up to 5 unused PTO days into the next calendar year. Carried-over days expire as follows:

US and UK: March 31
Canada: June 30
Any balance above 5 days is forfeited on December 31, unless local law requires otherwise. An employee who could not take leave because of illness or parental leave should contact People Operations, since different carryover rules may apply.

5.3 Requesting time off
Request PTO in Trellis, with the following minimum notice:

Length of absence	Minimum notice
1 to 2 days	3 business days
3 to 9 days	2 weeks
10 days or more	30 calendar days
Managers should respond within 3 business days. A request that receives no response in that time is escalated automatically to the manager's manager. It is not automatically approved.

5.4 Public holidays
Larkspur observes 10 public holidays in the US, 8 in the UK, and 11 in Canada, as listed each December on the People Operations intranet page. Employees required to work on a public holiday receive a substitute day off.

Larkspur also closes all offices between December 24 and January 1 in most years. This Winter Closure does not reduce PTO balances, but it does not apply to Customer Support or on-call staff, who receive equivalent days off at another time.

5.5 Peak Season Freeze
Freight volume peaks late in the year. From November 15 to December 5, Platform Engineering and Customer Support staff may not take PTO of more than 3 consecutive working days without VP approval. Production deployments during this period also need change board approval. The freeze does not apply to sick leave, parental leave, or bereavement leave.

5.6 Sick leave
Region	Entitlement
US	10 paid days per calendar year
Canada	10 paid days per calendar year
UK	Up to 20 working days at full pay per rolling 12 months, then Statutory Sick Pay
Tell your manager as early as possible on the first day of absence. Unused sick leave does not carry over and is not paid out on leaving.

Medical evidence: US and Canadian employees must provide a doctor's note for absences of more than 5 consecutive working days. UK employees self-certify for the first 7 calendar days and must provide a fit note after that.

5.7 Parental leave
Employees become eligible after 6 months of service.

Type	Paid leave
Primary caregiver	18 weeks at full pay
Secondary caregiver	8 weeks at full pay
This leave applies to birth, adoption, and surrogacy, and must start within 12 months of the child's arrival. Company-paid leave runs at the same time as, and is not added to, statutory leave. Employees should give at least 8 weeks' notice where possible. Returning employees may work a 4-day week at full pay for their first 4 weeks back.

5.8 Bereavement leave
Employees receive up to 5 paid days for the death of an immediate family member (spouse or partner, child, parent, sibling, or a household member) and up to 2 paid days for an extended family member (grandparent, grandchild, in-law, aunt, uncle, niece, nephew, or cousin). Additional unpaid leave may be granted by People Operations.

5.9 Jury and civic duty
Larkspur pays regular wages for up to 10 working days of jury duty per calendar year. Please give your manager a copy of the summons as soon as you receive it. Employees receive up to 2 paid hours to vote where voting hours overlap with work.

5.10 Volunteer days
Regular employees get 2 paid volunteer days per calendar year for registered charities. These days don't carry over.

5.11 Sabbatical
After 7 years of continuous service, employees qualify for a 4-week paid sabbatical, and again after every further 7 years. A sabbatical must be taken within 24 months of qualifying and requires 90 days' notice. It cannot be combined with more than 1 additional week of PTO, and cannot overlap with the Peak Season Freeze for affected teams.

6. Compensation
6.1 Pay schedule
Region	Frequency	Pay date
US	Semi-monthly	15th and last day of each month
UK	Monthly	25th of each month
Canada	Biweekly	Every second Friday
If a pay date falls on a weekend or bank holiday, payment is made on the previous business day. Report suspected payroll errors to payroll@larkspurfreight.example within 30 days.

6.2 Merit increases
Merit increases are based on the Year-End Review (Section 11.2) and take effect on April 1. Employees who started on or after October 1 of the previous year aren't eligible until the following cycle.

6.3 Annual bonus
Regular employees are eligible for an annual bonus, with the following targets as a percentage of base salary:

Level	Target bonus
L1 to L3	5%
L4 to L5	10%
L6 to L7	15%
Director	20%
Vice President	30%
The actual payout depends on Company results (weighted 60%) and individual results (weighted 40%). Bonuses are paid by March 15 for the previous calendar year. You must be employed and not under notice on the payment date. Employees hired during the year get a prorated bonus; those hired on or after October 1 aren't eligible until the next year. Employees rated "Not Meeting" receive no individual component.

Sales staff on a commission plan don't participate in the annual bonus.

6.4 Equity
Eligible full-time employees at L3 and above may receive stock options, subject to board approval. Grants vest over 4 years with a 1-year cliff: 25% vests on the first anniversary, then the rest vests monthly over 36 months. Vested options may be exercised for up to 90 days after employment ends.

6.5 Employee referral bonus
Role type	Bonus
Engineering and Security	$5,000
All other roles	$3,000
Bonuses are paid in the local currency equivalent once the new hire has completed 90 days of employment, provided the referring employee is still employed. Directors and above, recruiters, and the hiring manager for the role aren't eligible.

6.6 Overtime
Non-exempt US employees and hourly Canadian employees must get manager approval before working overtime. Overtime is paid in line with applicable law. UK employees aren't paid overtime unless stated in their contract, but may agree time off in lieu with their manager.

7. Benefits
7.1 Health coverage start date
Coverage starts on the first day of the month following your start date. If you start on the first day of a month, coverage starts that same day. Enroll within 30 days of your start date. Otherwise you must wait for the open enrollment period, held each year from October 15 to November 5, unless you have a qualifying life event.

7.2 US medical plans
Plan	Employee premium (monthly)	Deductible (individual)	Out-of-pocket max (individual)	HSA eligible
Larkspur Base (HDHP)	$0	$3,000	$6,500	Yes
Larkspur Plus (PPO)	$85	$1,000	$4,000	No
Larkspur Premier (PPO)	$160	$250	$2,500	No
Employees on the Base plan receive a Company HSA contribution of $1,000 per year for individual coverage and $2,000 for family coverage. Larkspur pays 100% of the premium for dental and vision.

7.3 UK and Canadian health benefits
UK: Private medical insurance through a Company-paid group plan, including cover for dependants, and a dental cash plan up to £600 per year.
Canada: A Company-paid extended health and dental plan that supplements provincial coverage, with a C$1,000 annual paramedical limit and a C$500 vision limit every 2 years.
7.4 Retirement
Region	Plan	Employer contribution	Vesting
US	401(k)	100% match on the first 4% of pay	Immediate
UK	Workplace pension	5% employer with a minimum 5% employee contribution	Immediate
Canada	Group RRSP	100% match on the first 4% of pay	After 2 years
7.5 Learning budget
US	UK	Canada
$1,500 per year	£1,200 per year	C$2,000 per year
The budget covers courses, certifications, books, and conferences related to your current role or a realistic next role. It's available from your start date, resets on January 1, and doesn't roll over. Any single purchase above $2,500 (or the local equivalent) requires VP approval.

If you leave within 6 months of a Company-paid certification costing more than $1,000, you may be asked to repay the cost where local law allows.

7.6 Wellness
Regular employees receive a wellness allowance of $40, £30, or C$55 per month, which may be used for gyms, fitness apps, or mental health services. Unused amounts expire at the end of each calendar quarter.

7.7 Employee Assistance Program
ClearPath is Larkspur's confidential Employee Assistance Program. Employees and their household members get 6 free counseling sessions per issue, per year, along with legal and financial consultations. ClearPath is available 24/7 at 1-800-555-0142 (US and Canada) or 0800 555 0142 (UK). Larkspur receives only anonymous usage statistics.

8. Expenses and Travel
8.1 General principles
Spend Company money as carefully as you would your own. Submit expense claims in Ledgerline within 30 days of the expense. Claims submitted after 90 days will not be reimbursed without CFO approval. Approved expenses are reimbursed in the next payroll cycle.

An itemized receipt is required for any expense of $25 or more (or the local equivalent). Receipts are required for all hotel and airfare expenses, regardless of amount.

8.2 Approval limits
Amount (per expense or trip)	Approver
Up to $500	Line manager
$500.01 to $5,000	Director
$5,000.01 to $25,000	VP
Over $25,000	VP and CFO
You cannot approve your own expenses, or those of anyone senior to you. Software purchases must go through IT regardless of amount (Section 9.6).

8.3 Booking travel
Book flights and hotels through Waypoint, the Company's travel portal, at least 14 days before departure where possible. Bookings outside Waypoint may not be reimbursed unless they cost at least 15% less, and any such booking also needs manager approval.

8.4 Air and rail
Flight duration (per segment)	Cabin allowed
Under 6 hours	Economy
6 hours or more	Premium economy
Any duration, business class	VP approval required
Rail travel is standard class, except that journeys over 3 hours may be booked in first class if the fare difference is under $50 or £40.

8.5 Hotels
Location	Nightly cap (before tax)
New York, San Francisco, London, Zurich	$350
All other locations	$225
UK employees should apply the cap as £275 and £180 respectively. Canadian employees should apply C$475 and C$300.

8.6 Meals
While traveling on business, meal expenses are reimbursed at actual cost, up to a daily limit of $75 domestic and $100 international. Limits are per person. Client meals are limited to $125 per person, and the claim must list the names and companies of attendees.

Alcohol is reimbursable only when served with a client or a VP-approved team event, up to 2 drinks per person. Minibar charges, personal entertainment, fines, and traffic tickets aren't reimbursable.

8.7 Mileage and ground transportation
Personal vehicle use for business is reimbursed at $0.70 per mile, £0.45 per mile, or C$0.72 per kilometer. Ordinary commuting to your assigned office isn't reimbursable. Ride-share and taxis are reimbursable for business travel. Rental cars are midsize or smaller.

8.8 Corporate cards
Directors and above, and employees who travel more than 6 times per year, may request a corporate card. Corporate cards are for business expenses only. Reconcile card transactions in Ledgerline by the 5th of the following month. Personal charges must be repaid within 15 days, and repeated misuse may lead to disciplinary action.

9. Information Security
9.1 Account security
Multi-factor authentication (MFA) is required on all Company accounts. Hardware security keys are required for Platform Engineering, Finance, and anyone handling Restricted data.
Passwords must be at least 14 characters, unique to each service, and stored in the Company password manager. Larkspur doesn't require periodic password changes unless a compromise is suspected.
Screens must lock after 5 minutes of inactivity.
9.2 Data classification
Class	Examples	Rules
Public	Marketing pages, published documentation	No restrictions
Internal	This handbook, org charts, internal wikis	Employees and approved contractors only
Confidential	Customer contracts, pricing, source code, financial forecasts	Need-to-know; encrypted in transit and at rest; sharing outside Larkspur needs an NDA
Restricted	Payroll data, health data, customer shipment records with personal data, credentials and secrets	Named individuals only; access logged and reviewed quarterly; never sent over email or chat
If you are unsure how to classify data, treat it as Confidential and ask the Security team.

9.3 Generative AI tools
Employees may use only the AI tools on the Approved AI Tools List, published on the Security intranet page.

Public and Internal data may be entered into any approved tool.
Confidential data may be entered only into tools marked "Enterprise Tier" on the list.
Restricted data must never be entered into any AI tool.
Employees remain responsible for checking AI output. Customer-facing use of AI-generated content requires human review. Using an unapproved tool with Company data is a security incident and should be reported under Section 9.5.

9.4 Devices
Company laptops are refreshed every 4 years. Critical security patches must be installed within 48 hours of release, and all other patches within 7 days; devices that remain out of date lose network access. Personal devices may access email and chat only through the managed mobile app, and may not store Confidential or Restricted data.

9.5 Reporting incidents and lost devices
Report a lost or stolen device or a suspected security incident within 1 hour of discovering it. Contact security@larkspurfreight.example, or call the 24-hour Security line at +1-555-0117. You won't be disciplined for honestly reporting a mistake promptly.

Severity	Definition	Response target
Sev 1	Customer-wide outage, or confirmed breach of Restricted data	15 minutes
Sev 2	Major feature down, or suspected data exposure	1 hour
Sev 3	Limited impact, with a workaround available	1 business day
Sev 4	Minor issue or request	5 business days
9.6 Software purchases
All software, including free tools and browser extensions that access Company data, requires an IT and Security review through the HelpDock portal. The standard review takes 10 business days.

9.7 Security training
All employees must finish security awareness training within 14 days of starting and every 12 months after that. Accounts of employees who are more than 30 days overdue are suspended until training is complete.

10. Code of Conduct
10.1 Respect at work
Larkspur prohibits discrimination, harassment, bullying, and retaliation of any kind. This applies in offices, online, at customer sites, on business travel, and at Company events.

10.2 Reporting concerns
You can raise concerns with any of the following:

your manager, or your manager's manager;
your People Partner;
Legal, at legal@larkspurfreight.example;
SpeakUp, the independent ethics hotline, at 1-800-555-0199 or 0800 555 0199 (UK), which accepts anonymous reports.
Managers who receive a report must pass it to People Operations within 1 business day. All reports are acknowledged within 2 business days, and investigations are normally completed within 30 calendar days. Retaliation against anyone who reports in good faith is itself a serious violation.

10.3 Gifts and hospitality
Employees may accept or give gifts worth up to $100 per person, per calendar year, from any one business partner, provided nothing is expected in return. Gifts above that amount must be declared to Legal within 5 business days. Cash and cash equivalents are never allowed. Gifts of any amount to government officials require prior approval from Legal.

10.4 Conflicts of interest
Disclose any outside employment, board seat, or financial interest that could conflict with your role, using the Trellis disclosure form. Holding less than 1% of a publicly traded company doesn't need to be disclosed. Outside work for a competitor, customer, or carrier partner isn't allowed without written approval from the General Counsel.

10.5 Relationships at work
Relationships between a manager and anyone in their reporting line must be disclosed to People Operations within 10 business days, so that reporting lines can be changed.

10.6 Alcohol and drugs
Employees may not work while impaired. Moderate alcohol consumption at Company-sponsored events is permitted, but employees are expected to behave responsibly.

10.7 Social media and public statements
Only Communications may speak on the Company's behalf. Refer press inquiries to press@larkspurfreight.example. Don't share Confidential or Restricted information publicly, and make clear that personal views are your own.

10.8 Disciplinary process
Depending on severity, consequences may include verbal warning, written warning, final written warning, or dismissal. Written warnings stay active for 12 months. Serious misconduct, such as theft, violence, or harassment, may lead to immediate dismissal. UK employees may appeal any formal disciplinary decision within 5 working days.

11. Performance and Growth
11.1 One-on-ones and goals
Managers and direct reports should meet at least every 2 weeks. Employees set goals each quarter and record them in Trellis.

11.2 Review cycle
Larkspur runs two reviews per year:

Mid-Year Check-In (April): Developmental feedback. No rating is assigned.
Year-End Review (October to November): A formal rating, calibrated by leadership in December, that informs merit increases and bonuses.
Ratings are Exceeding, Strong, Meeting, Developing, and Not Meeting. Employees with less than 3 months' service at the start of a cycle are not rated.

11.3 Performance Improvement Plans
A Performance Improvement Plan (PIP) typically lasts 60 calendar days, with check-ins at least every 2 weeks. A PIP can be extended once by up to 30 days. Employees on a PIP aren't eligible for promotion or internal transfer, and don't receive a merit increase that cycle.

11.4 Promotions
Promotion decisions are made twice a year, taking effect on April 1 and October 1. Employees must normally have spent at least 12 months at their current level. Nominations come from managers and are reviewed by a calibration panel. Promotion increases are separate from merit increases.

11.5 Mentorship
Larkspur's Co-Pilot program pairs employees with a mentor outside their reporting line for 6 months. Enrollment opens in February and August.

12. Leaving Larkspur
12.1 Notice periods
Region	During probation	After probation (L1 to L5)	After probation (L6 and above)
US	None required	2 weeks requested	4 weeks requested
Canada	As required by law	2 weeks requested	4 weeks requested
UK	1 week	1 month	3 months
Employees in the UK may have different periods in their contracts, and the contract governs. Larkspur may ask an employee not to work out their notice period, in which case pay continues as law or contract requires.

12.2 PTO on departure
US: Accrued, unused PTO is paid out where state law requires. Elsewhere, payout is capped at 10 days.
Canada: Accrued PTO is paid out in line with provincial law.
UK: Accrued, untaken statutory and contractual holiday is paid out. Holiday taken above the accrued amount may be deducted from final pay.
12.3 Returning equipment
All Company equipment must be returned within 10 business days of your last day. People Operations will send a prepaid shipping kit to remote employees. Larkspur may deduct the value of unreturned equipment where local law allows.

12.4 Benefits after leaving
US medical coverage ends on the last day of the month in which employment ends, and COBRA continuation may be available. Canadian extended health coverage ends on the last day of employment. UK private medical cover ends on the last day of employment. Allowances stop on the last day of employment.

12.5 Exit interviews and references
People Operations offers a voluntary exit interview during the final week. Employment references must come from People Operations and confirm only dates of employment and job title, unless the former employee gives written consent to share more.

12.6 Rehire
Former employees who return within 12 months have their earlier service counted for PTO accrual and sabbatical eligibility. Any unvested equity forfeited on departure isn't reinstated.

Appendix A: Glossary
Term	Meaning
Anchor days	Tuesday and Thursday; the days hybrid employees work from the office
CISO	Chief Information Security Officer
EAP	Employee Assistance Program; provided by ClearPath
Four Bearings	Larkspur's four company values
HelpDock	IT support and software request portal
Ledgerline	Expense reporting system
PIP	Performance Improvement Plan
Peak Season Freeze	November 15 to December 5, when PTO and deployments are restricted for certain teams
People Partner	The People Operations contact assigned to your department
PTO	Paid time off
SpeakUp	Independent, anonymous ethics hotline
Trellis	HR system for profiles, PTO, goals, and disclosures
Waypoint	Corporate travel booking portal
Winter Closure	Office closure between December 24 and January 1
Appendix B: Key Contacts
Need	Contact
HR and policy questions	people@larkspurfreight.example
Payroll	payroll@larkspurfreight.example
Benefits	benefits@larkspurfreight.example
Expenses and corporate cards	finance-help@larkspurfreight.example
IT support	HelpDock portal, or +1-555-0123
Security incidents and lost devices	security@larkspurfreight.example, or +1-555-0117 (24 hours)
Legal	legal@larkspurfreight.example
Press inquiries	press@larkspurfreight.example
Ethics hotline (SpeakUp)	1-800-555-0199; UK 0800 555 0199
Employee Assistance Program (ClearPath)	1-800-555-0142; UK 0800 555 0142
Appendix C: Revision History
Version	Effective date	Changes
4.2	July 1, 2026	Raised the US home office stipend from $500 to $600. Added Enterprise Tier rules to the generative AI policy (Section 9.3).
4.1	January 1, 2026	Raised the US learning budget from $1,000 to $1,500. Reduced the hybrid requirement from 3 days to 2 days per week, except for Manchester Customer Support. Dropped Wednesday as an anchor day.
4.0	January 1, 2025	Extended primary caregiver leave from 14 weeks to 18 weeks. Removed the 90-day password rotation requirement. Replaced the previous expense tool with Ledgerline. Raised the Work From Abroad cap from 10 to 20 working days per year.
3.5	March 1, 2024	Added the Work From Abroad policy, initially capped at 10 working days per year.
3.0	January 1, 2022	Moved the handbook to a single global edition covering the US, UK, and Canada.
Appendix D: Acknowledgment
Employees acknowledge this handbook in Trellis within 14 days of starting, and within 14 days of any major revision. Questions should go to people@larkspurfreight.example.