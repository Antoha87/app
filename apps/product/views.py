from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from models import Category, Phone
import re


class IndexView(TemplateView):
    template_name = 'product/index.html'


class RegExpView(TemplateView):
    template_name = 'product/reg_exp.html'
    str = 'asdfd((asdf)(asdf'

    def without_reg(self):
        i = max([index for index, sym in enumerate(self.str) if sym in ')'])
        if self.str[i] == '(':
            return self.str[:i]
        else:
            return self.str[:i+1]

    def with_reg(self):
        reg_str = re.sub('\([^)]+$', '', self.str)
        return reg_str

    def get_context_data(self, **kwargs):
        context = super(RegExpView, self).get_context_data(**kwargs)
        context['without_reg'] = self.without_reg()
        context['with_reg'] = self.with_reg()
        return context


class OrmView(ListView):
    template_name = 'product/orm.html'

    def get_queryset(self):
        return Category.custom_objects.all()


class QuestionsView(TemplateView):
    template_name = 'product/questions.html'


class DiscountView(TemplateView):
    template_name = 'product/discount.html'


class SqlView(TemplateView):
    template_name = 'product/sql.html'

    def get_context_data(self, **kwargs):
        context = super(SqlView, self).get_context_data(**kwargs)
        context['buy_list'] = Phone.objects.get_buy_items()
        context['all_count_items'] = Phone.objects.get_all_count_items()
        return context


class GitView(TemplateView):
    template_name = 'product/git.html'