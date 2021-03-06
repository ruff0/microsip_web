procedures = {}
################################################################
####                                                        ####
####              PROCEDIMIENTOS INVENTARIOS                ####
####                                                        ####
################################################################

procedures[ 'SIC_PUERTA_DEL_TRIGGERS' ] = '''
    CREATE OR ALTER PROCEDURE SIC_PUERTA_DEL_TRIGGERS 
    as
    begin
        if (exists(
            select 1 from RDB$Triggers
            where RDB$Trigger_name = 'SIC_PUERTA_INV_DOCTOSIN_BU')) then
            execute statement 'drop trigger SIC_PUERTA_INV_DOCTOSIN_BU';
    end
    '''

procedures[ 'SIC_ALMACENES_AT' ] = '''
    CREATE OR ALTER PROCEDURE SIC_ALMACENES_AT 
    as
    begin
        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'ALMACENES' and rf.RDB$FIELD_NAME = 'SIC_INVENTARIANDO')) then
            execute statement 'ALTER TABLE ALMACENES ADD SIC_INVENTARIANDO SMALLINT DEFAULT 1';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'ALMACENES' and rf.RDB$FIELD_NAME = 'SIC_INVCONAJUSTES')) then
            execute statement 'ALTER TABLE ALMACENES ADD SIC_INVCONAJUSTES SMALLINT DEFAULT 0';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'ALMACENES' and rf.RDB$FIELD_NAME = 'SIC_INVMODIFCOSTOS')) then
            execute statement 'ALTER TABLE ALMACENES ADD SIC_INVMODIFCOSTOS SMALLINT DEFAULT 0';
    end
    '''

procedures['SIC_DOCTOSINDET_AT'] = '''
    CREATE OR ALTER PROCEDURE SIC_DOCTOSINDET_AT
    as
    BEGIN

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'DOCTOS_IN_DET' and rf.RDB$FIELD_NAME = 'SIC_FECHAHORA_U')) then
            execute statement 'ALTER TABLE DOCTOS_IN_DET ADD SIC_FECHAHORA_U FECHA_Y_HORA';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'DOCTOS_IN_DET' and rf.RDB$FIELD_NAME = 'SIC_USUARIO_ULT_MODIF')) then
            execute statement 'ALTER TABLE DOCTOS_IN_DET ADD SIC_USUARIO_ULT_MODIF USUARIO_TYPE';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'DOCTOS_IN_DET' and rf.RDB$FIELD_NAME = 'SIC_DETALLETIME_MODIFICACIONES')) then
            execute statement 'ALTER TABLE DOCTOS_IN_DET ADD SIC_DETALLETIME_MODIFICACIONES MEMO';
    END  
    '''

################################################################
####                                                        ####
####              FATURA GLOBAL                             ####
####                                                        ####
################################################################



procedures['SIC_FACTURAGLOBAL_DOCTOS_PV_AT'] = '''
    CREATE OR ALTER PROCEDURE SIC_FACTURAGLOBAL_DOCTOS_PV_AT
    as
    BEGIN
        /*if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'DOCTOS_PV' and rf.RDB$FIELD_NAME = 'TIPO_GEN_FAC')) then
            execute statement 'ALTER TABLE DOCTOS_PV ADD TIPO_GEN_FAC CHAR(1) CHARACTER SET NONE';
        
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'DOCTOS_PV' and rf.RDB$FIELD_NAME = 'ES_FAC_GLOBAL')) then
            execute statement 'ALTER TABLE DOCTOS_PV ADD ES_FAC_GLOBAL CHAR(1) CHARACTER SET NONE';*/
    END  
    '''

################################################################
####                                                        ####
####                 PROCEDIMIENTOS FILTROS                 ####
####                                                        ####
################################################################

procedures['SIC_FILTROS_ARTICULOS_AT'] = '''
    CREATE OR ALTER PROCEDURE SIC_FILTROS_ARTICULOS_AT
    as
    BEGIN
        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'ARTICULOS' and rf.RDB$FIELD_NAME = 'SIC_CARPETA_ID')) then
            execute statement 'ALTER TABLE ARTICULOS ADD SIC_CARPETA_ID ENTERO_ID';
    END  
    '''


################################################################
####                                                        ####
####         PROCEDIMIENTOS GENERACION DE POLIZAS           ####
####                                                        ####
################################################################

procedures['SIC_LIBRES_CLIENTES_AT'] = '''
    CREATE OR ALTER PROCEDURE SIC_LIBRES_CLIENTES_AT
    as
    BEGIN
        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CLIENTES' and rf.RDB$FIELD_NAME = 'CUENTA_1')) then
            execute statement 'ALTER TABLE LIBRES_CLIENTES ADD CUENTA_1 ENTERO_ID';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CLIENTES' and rf.RDB$FIELD_NAME = 'CUENTA_2')) then
            execute statement 'ALTER TABLE LIBRES_CLIENTES ADD CUENTA_2 ENTERO_ID';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CLIENTES' and rf.RDB$FIELD_NAME = 'CUENTA_3')) then
            execute statement 'ALTER TABLE LIBRES_CLIENTES ADD CUENTA_3 ENTERO_ID';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CLIENTES' and rf.RDB$FIELD_NAME = 'CUENTA_4')) then
            execute statement 'ALTER TABLE LIBRES_CLIENTES ADD CUENTA_4 ENTERO_ID';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CLIENTES' and rf.RDB$FIELD_NAME = 'CUENTA_5')) then
            execute statement 'ALTER TABLE LIBRES_CLIENTES ADD CUENTA_5 ENTERO_ID';
    END  
    '''

procedures['ventas_inicializar'] = '''
    CREATE OR ALTER PROCEDURE ventas_inicializar
    as
    begin
        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_FAC_VE' and rf.RDB$FIELD_NAME = 'SEGMENTO_1')) then
            execute statement 'ALTER TABLE LIBRES_FAC_VE ADD SEGMENTO_1 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_FAC_VE' and rf.RDB$FIELD_NAME = 'SEGMENTO_2')) then
            execute statement 'ALTER TABLE LIBRES_FAC_VE ADD SEGMENTO_2 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_FAC_VE' and rf.RDB$FIELD_NAME = 'SEGMENTO_3')) then
            execute statement 'ALTER TABLE LIBRES_FAC_VE ADD SEGMENTO_3 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_FAC_VE' and rf.RDB$FIELD_NAME = 'SEGMENTO_4')) then
            execute statement 'ALTER TABLE LIBRES_FAC_VE ADD SEGMENTO_4 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_FAC_VE' and rf.RDB$FIELD_NAME = 'SEGMENTO_5')) then
            execute statement 'ALTER TABLE LIBRES_FAC_VE ADD SEGMENTO_5 VARCHAR(99)';

        /*Libres CREDITOS */

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_DEVFAC_VE' and rf.RDB$FIELD_NAME = 'SEGMENTO_1')) then
            execute statement 'ALTER TABLE LIBRES_DEVFAC_VE ADD SEGMENTO_1 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_DEVFAC_VE' and rf.RDB$FIELD_NAME = 'SEGMENTO_2')) then
            execute statement 'ALTER TABLE LIBRES_DEVFAC_VE ADD SEGMENTO_2 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_DEVFAC_VE' and rf.RDB$FIELD_NAME = 'SEGMENTO_3')) then
            execute statement 'ALTER TABLE LIBRES_DEVFAC_VE ADD SEGMENTO_3 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_DEVFAC_VE' and rf.RDB$FIELD_NAME = 'SEGMENTO_4')) then
            execute statement 'ALTER TABLE LIBRES_DEVFAC_VE ADD SEGMENTO_4 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_DEVFAC_VE' and rf.RDB$FIELD_NAME = 'SEGMENTO_5')) then
            execute statement 'ALTER TABLE LIBRES_DEVFAC_VE ADD SEGMENTO_5 VARCHAR(99)';
    end
    '''

procedures['cuentas_por_pagar_inicializar'] = '''
    CREATE OR ALTER PROCEDURE cuentas_por_pagar_inicializar
    as
    BEGIN
        /*Libres cargos */

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CARGOS_CP' and rf.RDB$FIELD_NAME = 'SEGMENTO_1')) then
            execute statement 'ALTER TABLE LIBRES_CARGOS_CP ADD SEGMENTO_1 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CARGOS_CP' and rf.RDB$FIELD_NAME = 'SEGMENTO_2')) then
            execute statement 'ALTER TABLE LIBRES_CARGOS_CP ADD SEGMENTO_2 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CARGOS_CP' and rf.RDB$FIELD_NAME = 'SEGMENTO_3')) then
            execute statement 'ALTER TABLE LIBRES_CARGOS_CP ADD SEGMENTO_3 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CARGOS_CP' and rf.RDB$FIELD_NAME = 'SEGMENTO_4')) then
            execute statement 'ALTER TABLE LIBRES_CARGOS_CP ADD SEGMENTO_4 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CARGOS_CP' and rf.RDB$FIELD_NAME = 'SEGMENTO_5')) then
            execute statement 'ALTER TABLE LIBRES_CARGOS_CP ADD SEGMENTO_5 VARCHAR(99)';
    END
    '''

procedures['cuentas_por_cobrar_inicializar'] = '''
    CREATE OR ALTER PROCEDURE cuentas_por_cobrar_inicializar
    as
    BEGIN
        /*Libres cargos */

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CARGOS_CC' and rf.RDB$FIELD_NAME = 'SEGMENTO_1')) then
            execute statement 'ALTER TABLE LIBRES_CARGOS_CC ADD SEGMENTO_1 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CARGOS_CC' and rf.RDB$FIELD_NAME = 'SEGMENTO_2')) then
            execute statement 'ALTER TABLE LIBRES_CARGOS_CC ADD SEGMENTO_2 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CARGOS_CC' and rf.RDB$FIELD_NAME = 'SEGMENTO_3')) then
            execute statement 'ALTER TABLE LIBRES_CARGOS_CC ADD SEGMENTO_3 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CARGOS_CC' and rf.RDB$FIELD_NAME = 'SEGMENTO_4')) then
            execute statement 'ALTER TABLE LIBRES_CARGOS_CC ADD SEGMENTO_4 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CARGOS_CC' and rf.RDB$FIELD_NAME = 'SEGMENTO_5')) then
            execute statement 'ALTER TABLE LIBRES_CARGOS_CC ADD SEGMENTO_5 VARCHAR(99)';


        /*Libres CREDITOS */

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CREDITOS_CC' and rf.RDB$FIELD_NAME = 'SEGMENTO_1')) then
            execute statement 'ALTER TABLE LIBRES_CREDITOS_CC ADD SEGMENTO_1 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CREDITOS_CC' and rf.RDB$FIELD_NAME = 'SEGMENTO_2')) then
            execute statement 'ALTER TABLE LIBRES_CREDITOS_CC ADD SEGMENTO_2 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CREDITOS_CC' and rf.RDB$FIELD_NAME = 'SEGMENTO_3')) then
            execute statement 'ALTER TABLE LIBRES_CREDITOS_CC ADD SEGMENTO_3 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CREDITOS_CC' and rf.RDB$FIELD_NAME = 'SEGMENTO_4')) then
            execute statement 'ALTER TABLE LIBRES_CREDITOS_CC ADD SEGMENTO_4 VARCHAR(99)';

        if (not exists(
        select 1 from RDB$RELATION_FIELDS rf
        where rf.RDB$RELATION_NAME = 'LIBRES_CREDITOS_CC' and rf.RDB$FIELD_NAME = 'SEGMENTO_5')) then
            execute statement 'ALTER TABLE LIBRES_CREDITOS_CC ADD SEGMENTO_5 VARCHAR(99)';
    END
    '''