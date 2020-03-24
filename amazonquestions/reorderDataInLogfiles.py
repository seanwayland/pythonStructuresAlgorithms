#https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        let_logs = []
        for log in logs:
			# only split in two chunks
            _, phrase = log.split(" ", 1)
            # take the first word and check if it's alpha
            
            if phrase.split(" ",1)[0].isalpha():
                let_logs.append(log)
            else:
                digit_logs.append(log)
        return (
            # we order it taking the phrase first and then the id 
            sorted(let_logs, key=lambda x: x.split(" ",1)[::-1]) 
            # since we want the digit logs in original order there is no need to order it
            + digit_logs
        )
