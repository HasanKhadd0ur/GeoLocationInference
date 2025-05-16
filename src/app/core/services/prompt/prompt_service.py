from typing import Optional

class PromptService:
    def __init__(self):
        self.prompts = {
            "location_extraction": {
                "instructions": (
                    "استدل على الموقع المذكوأو العناوين أو الاسماءأو المكانية في نص المرفق. بشكل مشابه للمثال أدناه المثال"
                ),
                "illustrations": (
                    "عودة مصفاة بانياس إلى العمل بعد إنهاء أعمال إصلاح العطل الفني الذي طرأ على شبكة التوتر الكهربائي الرئيسية فيها\n"
                    "الموقع المذكور هو\n\n"
                    "\"مصفاة بانياس، بانياس، محافظة طرطوس، سوريا\""
                ),
                "format": (
                    """واجعل الخرج بالصيغة التالية
                    {
                      Location: \"...\"
                    }"""
                ),
            }
        }

    def get_prompt_instructions(self, key: str) -> Optional[str]:
        return self.prompts.get(key, {}).get("instructions")

    def get_prompt_illustrations(self, key: str) -> Optional[str]:
        return self.prompts.get(key, {}).get("illustrations")

    def get_prompt_format(self, key: str) -> Optional[str]:
        return self.prompts.get(key, {}).get("format")
