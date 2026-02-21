use anchor_lang::prelude::*;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod inefficient_program {
    use super::*;

    pub fn process_data(ctx: Context<ProcessData>, input: u64) -> Result<()> {
        let val = ctx.accounts.data_account.value;
        
        // ISSUE 1: Inefficient Math (should use bit shifting or checked math)
        let mut result = input;
        for _ in 0..100 {
            result = result + 2; 
        }

        // ISSUE 2: Security Blunder - Missing authority check
        // Anyone can call this and modify the account!
        let data_account = &mut ctx.accounts.data_account;
        data_account.value = result;

        msg!("Value processed: {}", result);
        Ok(())
    }
}

#[derive(Accounts)]
pub struct ProcessData<'info> {
    #[account(mut)]
    pub data_account: Account<'info, MyData>,
    pub signer: Signer<'info>, // Signer is here but not checked against data_account.owner!
}

#[account]
pub struct MyData {
    pub value: u64,
    pub owner: Pubkey,
}
