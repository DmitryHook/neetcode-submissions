class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()

        for email in emails:
            local, domain = email.split('@', 1)
            local = local.split('+', 1)[0]
            local = local.replace('.', '')
            result.add(local + '@' + domain)

        return len(result)