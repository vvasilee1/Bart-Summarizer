from transformers import BertTokenizer,BertForConditionalGeneration

class SummarizerPipeline:
    def __init__(self,text:str):
        self.tokenizer = BertTokenizer.from_pretrained('facebook/bert-large-cnn')
        self.model = BertForConditionalGeneration.from_pretrained('facebook/bert-large-cnn')
        self.text = text
    def summarize(self,text:str):
        input_ids = self.tokenizer.encode(text,return_tensors='pt')
        summary_ids = self.model.generate(input_ids)
        summary = self.tokenizer.decode(summary_ids[0],skip_special_tokens=True)
        return summary