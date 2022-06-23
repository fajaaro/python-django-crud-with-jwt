class Repository:
    def update(self, model):
        return model.save()

    def delete(self, model):
        return model.delete()