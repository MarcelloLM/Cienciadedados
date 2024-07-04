import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

st.title('EBAC - Curso Profissão: Cientista de Dados')
st.subheader('Módulo 14 | Scripting | Exercício 2')
st.write('Aluno: Marcello Lassalla')
st.write('Data: 2 de junho de 2024')

def plot_pivot_table(df: pd.DataFrame, 
                     value: str, 
                     index: str, 
                     func: str, 
                     ylabel: str, 
                     xlabel: str, 
                     opcao: str='nenhuma'
                    ) -> plt.Figure:
    fig, ax = plt.subplots(figsize=[15, 5])
    if opcao == 'nenhuma':
        pd.pivot_table(data=df, 
                       values=value, 
                       index=index,
                       aggfunc=func
                      ).plot(ax=ax)
    elif opcao == 'sort':
        pd.pivot_table(data=df, 
                       values=value, 
                       index=index,
                       aggfunc=func
                      ).sort_values(value).plot(ax=ax)
    elif opcao == 'unstack':
        pd.pivot_table(data=df, 
                       values=value, 
                       index=index,
                       aggfunc=func
                      ).unstack().plot(ax=ax)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    return fig

def main():
    months = st.sidebar.multiselect('Selecione os meses:', 
                                    ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
                                    default=['01'])

    for mes in months:
        sinasc = pd.read_csv(f'https://raw.githubusercontent.com/rhatiro/Curso_EBAC-Profissao_Cientista_de_Dados/main/Mo%CC%81dulo%2014%20-%20Scripting/database/input/SINASC_RO_2019_{mes}.csv')
        
        max_data = sinasc.DTNASC.max()[:7]

        st.write(f"### Dados do mês: {mes}")
        st.write(f"Data inicial: {sinasc.DTNASC.min()}")
        st.write(f"Data final: {sinasc.DTNASC.max()}")

        st.write("#### Quantidade de nascimentos")
        fig = plot_pivot_table(df=sinasc, 
                               value='IDADEMAE', 
                               index='DTNASC', 
                               func='count', 
                               ylabel='Quantidade de nascimentos', 
                               xlabel='Data de nascimento')
        st.pyplot(fig)

        st.write("#### Média da idade das mães por sexo")
        fig = plot_pivot_table(df=sinasc, 
                               value='IDADEMAE', 
                               index=['DTNASC', 'SEXO'], 
                               func='mean', 
                               ylabel='Média da idade das mães', 
                               xlabel='Data de nascimento', 
                               opcao='unstack')
        st.pyplot(fig)

        st.write("#### Média do peso dos bebês por sexo")
        fig = plot_pivot_table(df=sinasc, 
                               value='PESO', 
                               index=['DTNASC', 'SEXO'], 
                               func='mean', 
                               ylabel='Média do peso dos bebês', 
                               xlabel='Data de nascimento',
                               opcao='unstack')
        st.pyplot(fig)

        st.write("#### Mediana do APGAR1 por escolaridade das mães")
        fig = plot_pivot_table(df=sinasc, 
                               value='APGAR1', 
                               index='ESCMAE', 
                               func='median', 
                               ylabel='Mediana do APGAR1', 
                               xlabel='Escolaridade',
                               opcao='sort')
        st.pyplot(fig)

        st.write("#### Média do APGAR1 por gestação")
        fig = plot_pivot_table(df=sinasc, 
                               value='APGAR1', 
                               index='GESTACAO', 
                               func='mean', 
                               ylabel='Média do APGAR1', 
                               xlabel='Gestação',
                               opcao='sort')
        st.pyplot(fig)

        st.write("#### Média do APGAR5 por gestação")
        fig = plot_pivot_table(df=sinasc, 
                               value='APGAR5', 
                               index='GESTACAO', 
                               func='mean', 
                               ylabel='Média do APGAR5', 
                               xlabel='Gestação',
                               opcao='sort')
        st.pyplot(fig)

if __name__ == "__main__":
    main()
