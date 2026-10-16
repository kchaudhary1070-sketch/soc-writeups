## Tool
Splunk Enterprise (Free), running on Windows

## Data used
auth.log file (uploaded through Add Data > Upload, source type linux_secure)

## Search queries
- `index=main` : 3 events
- `index=main "Failed password"` : 2 events

## What I did
- Uploaded the auth.log file to Splunk.
- Ran the two searches above.
- Checked the time and other details of each event.

## What I observed
Each event shows a time and date. The time is the upload time, not the original log time, because the file did not have timestamps.

## What I learned
I learned how to see the time and other details of each event in Splunk.

## Key takeaway
Splunk lets us search all events in an index, and a keyword like "Failed password" shows only the matching events.

## Questions I had
None