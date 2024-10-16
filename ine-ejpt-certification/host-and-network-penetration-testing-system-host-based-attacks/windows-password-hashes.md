# Windows Password Hashes

* Windows Stores hashed user account password locally in the SAM (Security Accounts Manager) database.
* Hashing is the process of converting a piece of data into another value. A hashing function or algorithm is used to generate the new value. The result of a hashing algorithm is known as a hash or hash value.
* Authentication and verification of user credentials is facilitated by the Local Security Authority (LSA).
* Windows versions up to Windows Server 2003 utilize two different types of hashes:
  * <mark style="color:red;">LM</mark>
  * <mark style="color:red;">NTLM</mark>
* Windows disables LM hashing and utilies NTLM hashing from Windows Vista onwards.

## SAM Database

* Sam (Security Account Manager) is a database file that is responsible for managing user acounts and password on Windows. All user account passwords stored in the SAM database are hashed.
* The SAM database file cannot be copied while the  OS is running.
* The Windows NT kernel keeps the SAM database file locked and as a result, attacker typically utilize in-memory techniques and tools to dump SAM hahed from the LSASS process.
* In modern versions of Windows (up until Windows 10) the SAM database is encrypted with a syskey.

<mark style="color:purple;">NOTE:</mark> Elevated/Admimistrative privileges are required ir oder to access and interact with the LSASS process.

## LN (LanMan)

* LM is the default hashing algorithm that was implemented in Windows operating systems prior to NT 4.0.
* The protocol is used to hash user passwords, and the hashing process can be broken down into the following steps:
  * The password is broken into two seven-character chunks.
  * All characters are then converted into uppercase.
  * Each chunk is then hashed separately with the DES algorithm.
* LM hashing is generally considered to be a weak protocol and can easily be cracked, primarily because the password does not include salts, consequently making brute-force and rainbow table attacks effective against LM hashes.

## LN (LanMan)

<figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

## NTLM (NTHash)

* NTLM is a collection of authentication protocols that are utilized in Windows to facilitate authentication between computers. The authentication process involves using a valid username and password to authenticate successfully.
* When a user account is created, it is encrypted using the MD4 hashing algorithm, while the original password is disposed of.

#### NTLM improved upon LM in the following ways:

* Does not split the hash in to two chunks.
* Case sensitive.
* Allows the use of symbols and unicode characters.

<figure><img src="../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>
