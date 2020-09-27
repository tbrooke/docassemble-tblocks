from docassemble.base.core import DAList, DAEmpty
from docassemble.base.util import Individual

__all__ = ['CompanyList']

class CompanyList(DAList):
    def init(self, *pargs, **kwargs):
        super(CompanyList, self).init(*pargs, **kwargs)
        self.object_type = Individual
    
    @property
    def member(self):
        for person in self.elements:
            if hasattr(person,'relationship'):
                if person.relationship.lower() in ['member']:
                    return person
        return DAEmpty()
    
    @property
    def officer(self):
        """ Returns list of officers"""
        return self.has_relationship(['president','vice-president','secretary','treasurer','ceo','cto','cfo'])

    @property
    def director(self):
        """Returns directors"""
        return self.has_relationship( ['parent','guardian','father','mother',
                'legal guardian','step father','step mother','stepparent','step parent'])

    @property
    def investor(self):
        """Returns investors"""
        return self.has_relationship(['stock holder','member','partner','owner', 'investor'])
    
    @property
    def coclients(self):
        """Return a list of coclients"""
        return self.has_relationship(['co-client','coclient'])

    @property
    def siblings(self):
        """Return a list of siblings"""
        return self.has_relationship(['sibling','brother','sister','step sister','step brother',
            'stepsister','stepbrother','half brother','half sister','half sibling','foster brother',
            'foster sister','foster sibling'])
    
    def has_relationship(self, relationships):
        """Return a list of household memberships with the specified relationship attribute. Relationship may be a string or list of strings."""
        related = DAList(object_type=Individual, auto_gather=False,gathered=True)
        for person in self.elements:
            if hasattr(person,'relationship'):
                if isinstance(relationships, list):
                    if person.relationship.lower() in relationships:
                        related.append(person)
                else:
                    if person.relationship.lower() == relationships:
                        related.append(person)
        return related 
