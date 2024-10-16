# Windows Event Logs & Finding Evil

## Windows Event Logging Basics

* **Purpose:**
  * Windows Event Logs store logs from different system components (system, applications, ETW providers, services).
  * Used for analyzing application errors, security events, and diagnostic information.
* **Categories of Event Logs:**
  * **Application:** Logs related to application errors.
  * **System:** Logs related to the operating system.
  * **Security:** Logs security-related events like logins, policy changes.
  * **Setup:** Logs related to system setup activities.
  * **Forwarded Events:** Logs forwarded from other machines for central logging.
* **Accessing Event Logs:**
  * **Event Viewer:** Primary tool for accessing Windows Event Logs.
  * **APIs:** Programmatic access via Windows Event Log API.
  * **Saved Logs:** Event Viewer can open and display saved `.evtx` files.

### Anatomy of an Event Log

* **Primary Components:**
  * **Log Name:** Name of the event log (e.g., Application, System, Security).
  * **Source:** Software that logged the event.
  * **Event ID:** Unique identifier for the event.
  * **Task Category:** Describes the purpose or use of the event.
  * **Level:** Severity of the event (Information, Warning, Error, Critical, Verbose).
  * **Keywords:** Flags for categorizing events (e.g., "Audit Success").
  * **User:** User account active during the event.
  * **OpCode:** Identifies the specific operation reported.
  * **Logged:** Date and time when the event was logged.
  * **Computer:** Name of the computer where the event occurred.
  * **XML Data:** Event details in XML format with additional data.
* **Key Fields:**
  * **Event ID:** Useful for further research and understanding event specifics.
  * **Source:** Identifies the software or component responsible for the event.
  * **Description:** Provides detailed information about the event.

### Security Event Log Example: Event ID 4624

* **Significance:**
  * Indicates the creation of a logon session.
  * Contains details like "Logon ID" and "Logon Type."
* **Correlation:**
  * Use "Logon ID" to correlate with other related events.

#### Custom XML Queries in Event Viewer

* **Purpose:**
  * Streamline analysis by creating custom XML queries for related events.
* **Steps:**
  * Use "Filter Current Log" -> "XML" -> "Edit Query Manually."
  * Focus on specific fields like "SubjectLogonId" for targeted searches.

[For more information on XML filtering in the Windows Event Viewer](https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/advanced-xml-filtering-in-the-windows-event-viewer/ba-p/399761)

#### Useful Windows Event Logs

**Windows System Logs**

* **Event ID 1074:** System shutdown/restart details.
* **Event ID 6005:** Event Log Service startup (indicates system boot-up).
* **Event ID 6006:** Event Log Service stopped (indicates system shutdown).
* **Event ID 6013:** System uptime.
* **Event ID 7040:** Service status change.

**Windows Security Logs**

* **Event ID 1102:** Audit log cleared.
* **Event ID 1116:** Antivirus malware detection.
* **Event ID 1118:** Antivirus remediation activity started.
* **Event ID 1119:** Antivirus remediation succeeded.
* **Event ID 1120:** Antivirus remediation failed.
* **Event ID 4624:** Successful logon.
* **Event ID 4625:** Failed logon.
* **Event ID 4648:** Logon with explicit credentials.
* **Event ID 4656:** Handle to an object requested.
* **Event ID 4672:** Special privileges assigned to a new logon.
* **Event ID 4698:** Scheduled task created.
* **Event ID 4700/4701:** Scheduled task enabled/disabled.
* **Event ID 4702:** Scheduled task updated.
* **Event ID 4719:** System audit policy changed.
* **Event ID 4738:** User account changed.
* **Event ID 4771:** Kerberos pre-authentication failed.
* **Event ID 4776:** Domain controller attempted to validate credentials.
* **Event ID 5001:** Antivirus real-time protection configuration changed.
* **Event ID 5140:** Network share object accessed.
* **Event ID 5142:** Network share object added.
* **Event ID 5145:** Network share object access attempted.
* **Event ID 5157:** Windows Filtering Platform blocked a connection.
* **Event ID 7045:** Service installed on the system.

#### Key Takeaways

* **Understanding Normal Behavior:** Crucial for identifying anomalies and potential threats.
* **Centralized Log Management:** Essential for collecting, parsing, and alerting on events in real-time.
* **Regular Monitoring:** Helps in early detection and mitigation of threats.
* **Correlation with Other Logs:** Provides a holistic view of security events in the environment.

## Analyzing Evil With Sysmon & Event Logs

each title type...for my notes

**ChatGPT said:**

ChatGPT

#### Sysmon Basics

* **Sysmon**: Windows service and device driver that logs system activity to Windows event logs.
* **Sysmon Key Features**:
  * Logs process creation, network connections, and file changes.
  * Offers event IDs for different types of system activity (e.g., Event ID 1 for "Process Creation").
  * Uses an XML-based configuration file for granular control over logging.
* **Common Event IDs**:
  * Event ID 4624: New logon events.
  * Event ID 4688: Newly created processes.
  * Event ID 1: Process Creation (Sysmon).
  * Event ID 3: Network Connection (Sysmon).

#### Sysmon Installation

* Download Sysmon from [Microsoft Docs](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
*   Install Sysmon:

    ```bash
    bashCopy codesysmon.exe -i -accepteula -h md5,sha256,imphash -l -n
    ```
*   Apply a custom configuration:

    ```bash
    bashCopy codesysmon.exe -c filename.xml
    ```

***

#### Detection Example 1: Detecting DLL Hijacking

* **Focus on Event ID 7**: Logs "Module Load" events to detect DLL hijacks.
* Modify the Sysmon configuration to include all events.
* Example: Using `calc.exe` and `WININET.dll` for DLL hijacking detection.
* **Indicators of Compromise (IOCs)**:
  * `calc.exe` found outside of `System32` directory.
  * `WININET.dll` loaded outside `System32` by `calc.exe`.
  * Unsigned `WININET.dll` detected.

***

#### Detection Example 2: Detecting Unmanaged PowerShell/C# Injection

* **Managed vs Unmanaged Processes**:
  * Managed processes (e.g., PowerShell) require CLR to run C# code.
* **Process Hacker**: Useful for analyzing processes and detecting managed code.
  * Look for `.NET` runtime, `clr.dll`, and `clrjit.dll` in processes that don’t normally use them.
* Example: Injecting an unmanaged PowerShell-like DLL into `spoolsv.exe` to detect unusual behavior.

***

#### Detection Example 3: Detecting Credential Dumping

* **Common Tool**: Mimikatz, used to dump credentials from LSASS.
  * Command: `sekurlsa::logonpasswords`
* **Focus on Sysmon Event ID 10**: Logs "ProcessAccess" events to monitor LSASS access.
* **Indicators of Compromise (IOCs)**:
  * Suspicious processes accessing LSASS.
  * `SeDebugPrivilege` requests.
  * SourceUser different from TargetUser in `ProcessAccess` events.

## Event Tracing for Windows (ETW)



**Event Tracing for Windows (ETW)** is a high-speed, general-purpose tracing facility built into the Windows operating system. It uses a buffering and logging mechanism at the kernel level to trace events generated by both user-mode applications and kernel-mode drivers.

**Key Benefits of ETW**:

* **High-performance**: Lightweight with minimal performance impact.
* **Comprehensive**: Captures a wide range of system events, from process activity to network and file changes.
* **Real-time monitoring**: Ideal for real-time security monitoring and incident response.
* **Extensible**: Custom providers can be created to suit specific needs.
* **Robust Tooling**: Tools like Microsoft's Message Analyzer and PowerShell's `Get-WinEvent` simplify ETW log retrieval and analysis.

***

#### ETW's Versatility and Use in Threat Detection

* **Broad telemetry sources**: Captures detailed events, including system calls, network activity, process creation/termination, file and registry changes, etc.
* **Dynamic tracing**: Logs events in real-time, offering deep visibility into system behavior.
* **Customizable**: Allows selective enabling and configuration of event providers to align with specific security needs.

**Applications in Security**:

* Identifying anomalous behavior.
* Detecting security incidents.
* Facilitating forensic investigations.

***

#### ETW Architecture & Components

1. **Controllers**:
   * Initiate and manage trace sessions.
   * Enable/disable providers.
   * Example: `logman.exe` utility.
2. **Providers**:
   * Generate and log events.
   * Four types:
     * **MOF Providers**: Use Managed Object Format.
     * **WPP Providers**: Low-level kernel-mode tracing.
     * **Manifest-based Providers**: Use XML manifest files for flexible event generation.
     * **TraceLogging Providers**: Use the TraceLogging API for simplified event generation.
3. **Consumers**:
   * Subscribe to events for processing or analysis.
   * Events often directed to `.ETL` files, which allow for offline analysis.
4. **Channels**:
   * Organize and filter events based on characteristics.
   * Consumers can selectively subscribe to specific channels.
5. **ETL Files**:
   * Durable storage for events.
   * Enable offline analysis, long-term archiving, and forensics.
   * Support for seamless rotation and efficient storage management.

***

#### Notes

* **Kernel-mode & user-mode** event providers supported.
* High-volume event providers are often disabled by default to conserve resources.
* Only ETW provider events with a **Channel** property can be consumed by the event log.

## Interacting With ETW

**Logman Utility**: A pre-installed tool for managing Event Tracing for Windows (ETW) and tracing sessions. It allows for the creation, management, and investigation of tracing sessions, providing useful insights for security and incident response.

* **Key Functionality**:
  * Create, initiate, and stop tracing sessions.
  * Investigate system-wide tracing sessions with the `-ets` parameter.
  * Example command: `logman.exe query -ets` (shows active Event Tracing Sessions, including Sysmon).

***

#### Investigating Event Tracing Sessions

* Running `logman.exe query "EventLog-System" -ets` reveals important session details:
  * **Session Name**
  * **Max Log Size**
  * **Log Location**
  * **Subscribed Providers**
* For each provider in the session:
  * **Name / Provider GUID**: Unique identifier.
  * **Level**: Event filtering level (warning, info, critical, etc.).
  * **Keywords Any**: Event filters based on provider-specific keywords.

***

#### Querying ETW Providers

* **Command**: `logman.exe query providers` lists all available providers (over 1,000 in Windows 10).
* **Filtering**: Use `findstr` to narrow down results (e.g., `logman.exe query providers | findstr "Winlogon"`).
* **Provider Details**: Specifying a provider gives detailed information about:
  * Keywords for event filtering.
  * Event levels.
  * Processes using the provider.
  * Example: `logman.exe query providers Microsoft-Windows-Winlogon`.

***

#### GUI-based Alternatives

* **Performance Monitor Tool**:
  * Visualize running trace sessions.
  * Double-click a session for detailed information (engaged providers, features, etc.).
  * Modify or create sessions under the "User Defined" category.
* **EtwExplorer Project**: View ETW provider metadata using the EtwExplorer tool.

#### Useful ETW Providers

1. **Microsoft-Windows-Kernel-Process**:
   * Monitors process-related activity within the Windows kernel.
   * Detects malicious tactics like process injection and process hollowing.
2. **Microsoft-Windows-Kernel-File**:
   * Focuses on file operations.
   * Useful for detecting unauthorized file access, system file changes, and ransomware activities.
3. **Microsoft-Windows-Kernel-Network**:
   * Provides visibility into network-related activities.
   * Helps detect data exfiltration, unauthorized connections, and command-and-control (C2) communication.
4. **Microsoft-Windows-SMBClient/SMBServer**:
   * Monitors SMB client and server activity.
   * Useful for detecting lateral movement and data exfiltration through unusual SMB traffic.
5. **Microsoft-Windows-DotNETRuntime**:
   * Tracks .NET runtime events.
   * Ideal for identifying anomalies in .NET applications or malicious .NET assembly loading.
6. **OpenSSH**:
   * Monitors SSH connection attempts, authentication success/failure, and potential brute-force attacks.
7. **Microsoft-Windows-VPN-Client**:
   * Tracks VPN client events.
   * Detects unauthorized or suspicious VPN connections.
8. **Microsoft-Windows-PowerShell**:
   * Monitors PowerShell command execution.
   * Useful for detecting suspicious script execution or potential exploitation.
9. **Microsoft-Windows-Kernel-Registry**:
   * Monitors registry operations.
   * Detects changes associated with persistence mechanisms and malware installation.
10. **Microsoft-Windows-CodeIntegrity**:
    * Monitors code and driver integrity checks.
    * Detects attempts to load unsigned or malicious drivers.
11. **Microsoft-Antimalware-Service**:
    * Detects potential issues with the antimalware service, including service configuration changes or evasion techniques.
12. **WinRM (Windows Remote Management)**:
    * Monitors remote management activity.
    * Useful for detecting unauthorized remote command execution.
13. **Microsoft-Windows-TerminalServices-LocalSessionManager**:
    * Tracks local Terminal Services sessions.
    * Detects unauthorized remote desktop activity.
14. **Microsoft-Windows-Security-Mitigations**:
    * Monitors security mitigation operations.
    * Detects potential attempts to bypass security controls.
15. **Microsoft-Windows-DNS-Client**:
    * Provides visibility into DNS client activity.
    * Useful for detecting DNS-based attacks like tunneling or unusual requests indicating C2 communication.
16. **Microsoft-Antimalware-Protection**:
    * Monitors antimalware protection mechanisms.
    * Detects disabled protection features or configuration changes used by malware.

***

#### Restricted Providers

Certain ETW providers are restricted, offering valuable telemetry but accessible only to privileged processes. This helps safeguard sensitive system data.

1. **Microsoft-Windows-Threat-Intelligence**:
   * Provides deep insights into security threats.
   * Used in Digital Forensics and Incident Response (DFIR).
   * Access requires **Protected Process Light (PPL)** permissions, which are typically granted to anti-malware vendors with special Microsoft approval.
   * **Benefits**:
     * Records granular data about potential threats.
     * Aids in detecting sophisticated attacks and collecting forensic evidence.
     * Can be monitored in real-time to identify ongoing threats and prevent further damage.

## Tapping into ETW

Abnormal parent-child relationships among processes can be indicative of malicious activities. In standard Windows environments, certain processes never call or spawn others. For example, it is highly unlikely to see "calc.exe" spawning "cmd.exe" in a normal Windows environment. Understanding these typical parent-child relationships can assist in detecting anomalies. Samir Bousseaden has shared an insightful mind map introducing common parent-child relationships, which can be referenced [here](https://twitter.com/SBousseaden/status/1195373669930983424).

<figure><img src="../../.gitbook/assets/image (187).png" alt=""><figcaption></figcaption></figure>

#### Detection Example 1: Detecting Strange Parent-Child Relationships

* **Abnormal parent-child relationships** among processes can indicate malicious activity. Example: "calc.exe" spawning "cmd.exe" is unlikely in a normal environment.
* **Process Hacker** can visualize these relationships. For instance, if "spoolsv.exe" spawns "whoami.exe" (anomalous behavior), it should raise suspicion.
* **Example**: Using **Parent PID Spoofing**:
  * In this attack, "spoolsv.exe" appears to spawn "cmd.exe" through spoofing.
  * Tool: `psgetsystem` allows the manipulation of parent process IDs.
  * ETW logs from **SilkETW** can provide more accurate insight into actual process creation compared to Sysmon, showing PowerShell.exe as the true parent of "cmd.exe."

#### Detection Example 2: Detecting Malicious .NET Assembly Loading

* **Living off the Land (LotL)**: Attackers exploit legitimate system tools like PowerShell to reduce detection risk.
* **Bring Your Own Land (BYOL)**: Attackers now use custom .NET assemblies executed in memory, bypassing tools like PowerShell. This minimizes disk artifacts and can evade detection.
* **Key Features of BYOL**:
  * Windows has built-in .NET versions, and .NET allows managed code execution (e.g., garbage collection).
  * Loading .NET assemblies in memory avoids disk artifacts.
* **Detection Strategy**:
  * Monitor loading of key .NET DLLs like `clr.dll` and `mscoree.dll` using **Sysmon Event ID 7**.
  * Example: Executing a malicious assembly (e.g., Seatbelt) triggers the loading of these DLLs.
* **SilkETW for ETW**: Collect data from **Microsoft-Windows-DotNETRuntime provider** for detailed insights.
  * Target specific subsets of events like JIT, Interop, and Loader for information about assembly execution flow and interactions with unmanaged code.

These methods offer enhanced visibility into suspicious processes and behaviors that traditional Sysmon logging might miss.

## Get-WinEvent

#### Mass Analysis of Windows Event Logs and Sysmon Logs in Cybersecurity

Windows Event Logs and Sysmon logs provide crucial insights for Incident Response (IR) and threat hunting in cybersecurity. However, due to the large volume of logs generated daily, it is necessary to employ efficient tools and techniques for analysis.

One of the primary tools for this task is PowerShell’s **Get-WinEvent** cmdlet, which enables querying logs in bulk.

#### Key Concepts

* **Windows Event Logs**: Store detailed system, user activity, and event information.
* **Sysmon Logs**: Provide insights into system activities such as process creation, file modification, and network connections.

#### Using `Get-WinEvent`

The **Get-WinEvent** cmdlet in PowerShell allows querying and retrieving various types of logs, including:

* Classic logs like **System** and **Application** logs.
* Logs generated by **Windows Event Log** technology.
* **ETW** (Event Tracing for Windows) logs.

**Retrieving All Logs**

*   Use the `-ListLog *` parameter to get a list of all logs.

    ```powershell
    powershellCopy codeGet-WinEvent -ListLog * | Select-Object LogName, RecordCount, IsClassicLog, IsEnabled, LogMode, LogType | Format-Table -AutoSize
    ```

    This command provides information on:

    * **LogName**
    * **RecordCount** (number of events)
    * **IsClassicLog** (format type)
    * **LogMode** (Circular, Retain, AutoBackup)
    * **LogType** (Administrative, Operational, etc.)

**Retrieving Event Providers**

*   Use the `-ListProvider` parameter to retrieve event log providers associated with logs.

    ```powershell
    powershellCopy codeGet-WinEvent -ListProvider * | Format-Table -AutoSize
    ```

    Providers are sources of events and are linked to specific logs.

#### Querying Specific Logs

**Example 1: System Logs**

*   Retrieve the most recent 50 events from the **System** log:

    ```powershell
    powershellCopy codeGet-WinEvent -LogName 'System' -MaxEvents 50 | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message | Format-Table -AutoSize
    ```

**Example 2: Microsoft-Windows-WinRM/Operational Logs**

*   Retrieve the first 30 events from the **Microsoft-Windows-WinRM/Operational** log:

    ```powershell
    powershellCopy codeGet-WinEvent -LogName 'Microsoft-Windows-WinRM/Operational' -MaxEvents 30 | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message | Format-Table -AutoSize
    ```

**Example 3: Retrieving Oldest Logs**

*   Use the `-Oldest` parameter to get the first 30 events based on their creation time:

    ```powershell
    powershellCopy codeGet-WinEvent -LogName 'Microsoft-Windows-WinRM/Operational' -Oldest -MaxEvents 30 | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message | Format-Table -AutoSize
    ```

#### Analyzing .evtx Files

To analyze exported logs in `.evtx` format, use the `-Path` parameter:

```powershell
powershellCopy codeGet-WinEvent -Path 'C:\Tools\chainsaw\EVTX-ATTACK-SAMPLES\Execution\exec_sysmon_1_lolbin_pc
```



#### Filtering Events with `FilterHashtable` in Windows PowerShell

The `-FilterHashtable` parameter allows for precise filtering of Windows event logs. This feature is useful when monitoring logs for specific event types, such as suspicious network connections or process executions.

**Basic Usage**

The following example retrieves event logs from the **Sysmon Operational** log, filtering for **Event IDs 1 and 3**, which typically correspond to process creation and network connections:

```powershell
powershellCopy codeGet-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; ID=1,3} |
Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message |
Format-Table -AutoSize
```

**Filtering by Date Range**

To filter logs between specific dates:

```powershell
powershellCopy code$startDate = (Get-Date -Year 2023 -Month 5 -Day 28).Date
$endDate   = (Get-Date -Year 2023 -Month 6 -Day 3).Date

Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; ID=1,3; StartTime=$startDate; EndTime=$endDate} |
Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message |
Format-Table -AutoSize
```

**Filtering Network Connection to Specific IP**

The script below identifies Sysmon Event ID 3 logs where a network connection was made to the IP `52.113.194.132`:

```powershell
powershellCopy codeGet-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; ID=3} |
ForEach-Object {
    $xml = [xml]$_.ToXml()
    $eventData = $xml.Event.EventData.Data
    New-Object PSObject -Property @{
        SourceIP = $eventData | Where-Object {$_.Name -eq "SourceIp"} | Select-Object -ExpandProperty '#text'
        DestinationIP = $eventData | Where-Object {$_.Name -eq "DestinationIp"} | Select-Object -ExpandProperty '#text'
        ProcessGuid = $eventData | Where-Object {$_.Name -eq "ProcessGuid"} | Select-Object -ExpandProperty '#text'
        ProcessId = $eventData | Where-Object {$_.Name -eq "ProcessId"} | Select-Object -ExpandProperty '#text'
    }
} | Where-Object {$_.DestinationIP -eq "52.113.194.132"}
```

**XML and XPath Filtering**

To detect suspicious DLL loading activities (e.g., `clr.dll` or `mscoree.dll`) using Sysmon’s Event ID 7:

```powershell
powershellCopy code$Query = @"
    <QueryList>
        <Query Id="0">
            <Select Path="Microsoft-Windows-Sysmon/Operational">
                *[System[(EventID=7)]] and *[EventData[Data='mscoree.dll']] or *[EventData[Data='clr.dll']]
            </Select>
        </Query>
    </QueryList>
"@

Get-WinEvent -FilterXml $Query | ForEach-Object {Write-Host $_.Message `n}
```

This method leverages Sysmon's ability to monitor DLL loads, allowing you to track potentially dangerous behaviors like process injections or the loading of uncommon binaries.

#### Advanced Techniques

You can filter events based on specific properties (e.g., CommandLine arguments, ProcessGuid) using either XPath or FilterHashtable.

For example, detecting **encoded PowerShell commands** in the Sysmon logs:

```powershell
powershellCopy codeGet-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; ID=1} |
Where-Object {$_.Properties[21].Value -like "*-enc*"} |
Format-List
```

This command checks for `Process Create` events where the `CommandLine` contains encoded commands (identified by `-enc`), a common indicator of obfuscated or malicious script execution.



















































