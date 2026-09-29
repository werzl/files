# Security Triage and SLAs

## If the triage will take longer than the fix
Just fix it


## SLAs
Software companies often agree SLA's (Service Level Agreements) with their customers.

They are a formal contract between a service provider and a customer, and define a level of service or standard of performance.

An example:
```
Customer Support SLAs
- GMT 9am-5pm, Monday to Friday
- Incident response and recovery
- Performance reports
- Response Times:
  - Response within 4 hours for high severity issues
  - Response within 1 day for medium severity issues
  - Response within 3 days for general issues

Software Vulnerability SLAs
- Critical - 14 days
- High - 28 days
- Medium - 60 days
```

These SLAs can be part of security compliance audits like SOC2.


## Triage
A triage process might look like this:
- Receive alert from security tooling/scanning that a new CVE has been found in your code
- What level of CVE is the issue? (C, H, M, L)
- Is the CVE exploitable?
  - Sometimes, even a critical CVE cannot be exploited in your system, this can happen if the vulnerable component is behind a system that is closed off to the outside world via a network policy, or maybe you consume a vulnerable package - but don't use the vulnerable component within that package.
  - If the CVE is high, but the impact is low or it isn't exploitable - you can take some extra steps (which can be useful, specially if the required fix is a big one)
    - Notify customers of the SLA breach, if you dont want to fix it right away
    - Downgrade the severity of the vulnerability
- Schedule work on the backlog to fix the vulnerability and hand off to the relevant engineers

