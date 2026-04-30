JURISDICTIONS = {
    "us": {
        "name": "United States",
        "source": "https://vote.gov/register/",
        "note": "Election rules and deadlines vary by state and territory. Confirm dates with the state or local election office.",
        "steps": [
            {
                "phase": "Eligibility",
                "title": "Confirm voter eligibility",
                "when": "Before registration opens or as early as possible",
                "details": "Check citizenship, age, residency, and any state-specific rules before starting registration.",
                "action": "Review your state requirements on Vote.gov.",
            },
            {
                "phase": "Registration",
                "title": "Register or update registration",
                "when": "Deadline varies by state; some are weeks before Election Day",
                "details": "Register if you are new, moved, changed your name, or need to update party affiliation for a primary.",
                "action": "Use Vote.gov to find your state registration page.",
            },
            {
                "phase": "Verification",
                "title": "Check registration status",
                "when": "After submitting and again before voting starts",
                "details": "Verify your name, address, party where applicable, and polling place.",
                "action": "Use your state election office lookup tool.",
            },
            {
                "phase": "Voting Plan",
                "title": "Choose how you will vote",
                "when": "Before early voting or absentee ballot deadlines",
                "details": "Options may include election-day voting, early in-person voting, mail voting, or absentee voting.",
                "action": "Check available methods and deadlines for your state.",
            },
            {
                "phase": "Preparation",
                "title": "Review ballot and ID requirements",
                "when": "One to two weeks before voting",
                "details": "Look up sample ballots, candidate lists, ballot measures, and accepted identification.",
                "action": "Bring required ID if your jurisdiction requires it.",
            },
            {
                "phase": "Voting",
                "title": "Cast and track your ballot",
                "when": "During the official voting period",
                "details": "Vote using your selected method. If voting by mail, track receipt where tracking is available.",
                "action": "Keep confirmation records until the election is certified.",
            },
        ],
    },
    "india": {
        "name": "India",
        "source": "https://voters.eci.gov.in/",
        "note": "Election schedules, voter rolls, and polling station details are published by the Election Commission of India and state election authorities.",
        "steps": [
            {
                "phase": "Eligibility",
                "title": "Check eligibility and documents",
                "when": "Before applying or updating voter details",
                "details": "Confirm age, citizenship, ordinary residence, and required identity/address documents.",
                "action": "Use the ECI voter services portal for current forms and instructions.",
            },
            {
                "phase": "Enrollment",
                "title": "Apply, shift, correct, or delete entry",
                "when": "During continuous updation or announced revision windows",
                "details": "Submit the appropriate form for new enrollment, address shift, correction, or deletion.",
                "action": "Track the application reference number after submission.",
            },
            {
                "phase": "Verification",
                "title": "Verify name in electoral roll",
                "when": "After processing and before the poll schedule",
                "details": "Search by EPIC number or personal details to confirm roll inclusion and polling part.",
                "action": "Download or note your voter details before polling day.",
            },
            {
                "phase": "Schedule",
                "title": "Review election schedule",
                "when": "After the commission announces dates",
                "details": "Check nomination, scrutiny, withdrawal, polling, counting, and result dates for your constituency.",
                "action": "Follow only official ECI or CEO announcements.",
            },
            {
                "phase": "Polling",
                "title": "Prepare for polling day",
                "when": "Before your constituency poll date",
                "details": "Locate your polling station, understand queue and assistance options, and carry accepted ID.",
                "action": "Use official voter helpline resources for booth information.",
            },
            {
                "phase": "Counting",
                "title": "Understand counting and results",
                "when": "On the notified counting date",
                "details": "Results are declared after counting and official processes are completed.",
                "action": "Use ECI result portals and official releases.",
            },
        ],
    },
    "uk": {
        "name": "United Kingdom",
        "source": "https://www.gov.uk/register-to-vote",
        "note": "Registration, voter authority certificate, postal vote, and proxy vote deadlines depend on the election.",
        "steps": [
            {
                "phase": "Eligibility",
                "title": "Check voting eligibility",
                "when": "Before registration",
                "details": "Eligibility depends on age, nationality, residence, and the type of election.",
                "action": "Use GOV.UK or the Electoral Commission guidance.",
            },
            {
                "phase": "Registration",
                "title": "Register or update details",
                "when": "Before the published registration deadline",
                "details": "Register again if your name, address, or nationality changes.",
                "action": "Use the GOV.UK registration service.",
            },
            {
                "phase": "Voting Method",
                "title": "Choose in person, postal, or proxy voting",
                "when": "Before postal or proxy vote deadlines",
                "details": "Apply early if you need a postal or proxy vote.",
                "action": "Check your local council or Electoral Commission instructions.",
            },
            {
                "phase": "Voter ID",
                "title": "Prepare accepted photo ID if required",
                "when": "Before polling day",
                "details": "Some elections require accepted photo ID at the polling station.",
                "action": "Apply for a voter authority certificate if needed.",
            },
            {
                "phase": "Voting",
                "title": "Cast your vote",
                "when": "During the official voting window",
                "details": "Vote at your polling station, return your postal vote, or use your proxy arrangement.",
                "action": "Follow the instructions on your poll card or postal voting pack.",
            },
            {
                "phase": "Results",
                "title": "Follow counting and declaration",
                "when": "After polls close",
                "details": "Votes are verified, counted, and declared by the returning officer.",
                "action": "Use council or Electoral Commission result pages.",
            },
        ],
    },
}

PERSONAS = {
    "first-time": "First-time voter",
    "returning": "Returning voter",
    "mail": "Mail, postal, or absentee voter",
    "overseas": "Overseas or away-from-home voter",
    "student": "Student or recently moved voter",
}

FAQ = [
    {
        "keywords": ["eligible", "eligibility", "age", "citizen", "citizenship"],
        "answer": "Start with eligibility because every later step depends on it. Check age, citizenship or nationality, residence, and any election-specific restrictions. Use the official source for your selected location before relying on a deadline or document list.",
    },
    {
        "keywords": ["register", "registration", "enroll", "enrollment", "roll"],
        "answer": "Registration or enrollment is the step that puts your name on the official voter list. If you moved, changed your name, or changed party affiliation where parties matter, update your record before the published deadline.",
    },
    {
        "keywords": ["deadline", "timeline", "date", "when", "schedule"],
        "answer": "Election timelines usually include registration deadlines, mail or postal ballot deadlines, early voting dates, polling day, counting, and certification or official declaration. The exact dates depend on the jurisdiction, so the app links to the official source for confirmation.",
    },
    {
        "keywords": ["id", "identification", "document", "proof"],
        "answer": "ID and document rules vary. Some places require photo ID at the polling place, some ask for documents during registration, and some allow alternatives. Check the official source for accepted documents before voting.",
    },
    {
        "keywords": ["mail", "postal", "absentee", "proxy", "overseas"],
        "answer": "Alternative voting methods usually require extra lead time. Request the ballot or proxy arrangement early, follow signing and return instructions exactly, and use tracking tools where available.",
    },
    {
        "keywords": ["count", "counting", "results", "certification", "certify"],
        "answer": "After voting closes, officials verify ballots, count eligible votes, resolve issues under local rules, publish results, and complete any certification or declaration process. Unofficial results can change before the official final result.",
    },
    {
        "keywords": ["poll", "polling", "booth", "station", "place"],
        "answer": "Polling-place information can change. Check your official voter record before voting, note the address and hours, bring required ID if applicable, and ask election staff for help if your name is not found.",
    },
]
