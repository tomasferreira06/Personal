# Clearing Windows Event Logs

The Windows OS stored and catalogs all actions/events performed on the system and stores them in the Windows Event Log.

* Event logs are categorized based on the type of events they store:
  * <mark style="color:red;">Application logs</mark>: Stored application/program events like startups, crashes etc..
  * <mark style="color:red;">System Logs</mark>: Stores system events like startups, reboots etc..
  * <mark style="color:red;">Security Logs:</mark> Stores security events like password changes, authentication failures etc...
* Event logs can be accessed via the Event Viewer on Windows

The event logs are the first stop for any forensic investigator after a compromise has been detected. It is therefore very important to clear your tracks after you are done with your assessment.

## Practice Demo

In this case the target is running the <mark style="color:red;">BadBlue</mark> application

* <mark style="color:yellow;">exploit/windows/http/badblue\_passthru</mark>

### Clearing the Logs

In the meterpreter session run:

* <mark style="color:yellow;">clearev</mark>

