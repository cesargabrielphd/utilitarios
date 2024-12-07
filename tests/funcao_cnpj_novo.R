library(dplyr)

calcular_proporcao_novos_cnpjs <- function(df, coluna_ano, coluna_cnpj) {
  df <- df %>% 
    select({{coluna_ano}}, {{coluna_cnpj}}) %>%
    distinct() %>% 
    rename(Ano_Base = {{coluna_ano}}, cnpj = {{coluna_cnpj}})
  
  df$CNPJ_novo <- FALSE
  acumulados <- c()
  
  for (ano in unique(df$Ano_Base)) {
    cnpj_atual <- df$cnpj[df$Ano_Base == ano]
    
    novos_cnpj <- setdiff(cnpj_atual, acumulados)
    
    df$CNPJ_novo[df$Ano_Base == ano & df$cnpj %in% novos_cnpj] <- TRUE
    
    acumulados <- unique(c(acumulados, cnpj_atual))
  }
  
  resultado <- df %>%
    group_by(Ano_Base) %>%
    summarize(
      CNPJs_novos = sum(CNPJ_novo, na.rm = TRUE),
      CNPJ_acumulados = n_distinct(cnpj),
      Proporcao_novos = CNPJs_novos / lag(CNPJ_acumulados, default = CNPJs_novos[1]),
      .groups = 'drop'
    )
  
  return(resultado)
}
